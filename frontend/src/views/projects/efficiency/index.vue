<template>
  <div class="app-container">
    <el-row :gutter="20">
      <!--部门数据-->
      <el-col :span="4" :xs="24">
        <div class="head-container">
          <el-input
            v-model="moduleName"
            placeholder="请输入模块名称"
            clearable
            size="small"
            prefix-icon="el-icon-search"
            style="margin-bottom: 20px"
          />
        </div>
        <div class="head-container">
          <el-tree
            ref="tree"
            :data="moduleOptions"
            :props="moduleProps"
            :expand-on-click-node="false"
            :filter-node-method="filterNode"
            default-expand-all
            @node-click="handleNodeClick"
          >
          </el-tree>
        </div>
      </el-col>
      <!--用户数据-->
      <el-col :span="20" :xs="24">
        <el-form v-show="showSearch" ref="queryForm" :model="queryParams" :inline="true" label-width="68px">
          <el-form-item label="名称" prop="moduleName">
            <el-input
              v-model="queryParams.moduleName"
              placeholder="请输入小工具名称"
              clearable
              size="small"
              style="width: 240px"
              @keyup.enter.native="handleQuery"
            />
          </el-form-item>
          <el-form-item label="状态" prop="is_active">
            <el-select
              v-model="queryParams.is_active"
              placeholder="请选择状态"
              clearable
              size="small"
              style="width: 240px"
            >
              <el-option
                v-for="dict in statusOptions"
                :key="dict.dictValue"
                :label="dict.dictLabel"
                :value="dict.dictValue"
              />
            </el-select>
          </el-form-item>
          <el-form-item v-if="false" label="创建时间">
            <el-date-picker
              v-model="dateRange"
              size="small"
              style="width: 240px"
              value-format="yyyy-MM-dd"
              type="daterange"
              range-separator="-"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
            />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
            <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
          </el-form-item>
        </el-form>
        <el-table v-loading="loading" :data="efficiencyList" @selection-change="handleSelectionChange">
          <el-table-column type="selection" width="50" align="center" />
          <el-table-column key="id" label="编号" align="center" prop="id" />
          <el-table-column
            key="name"
            label="名称"
            align="center"
            prop="name"
            :show-overflow-tooltip="true"
          />
          <el-table-column
            key="command"
            label="脚本"
            align="center"
            prop="command"
            :show-overflow-tooltip="true"
          />
          <el-table-column key="is_active" label="状态" align="center">
            <template slot-scope="scope">
              <el-switch
                v-model="scope.row.status"
                disabled
                @change="handleStatusChange(scope.row)"
              />
            </template>
          </el-table-column>
          <el-table-column label="创建时间" align="center" prop="create_datetime" width="160">
            <template slot-scope="scope">
              <span>{{ parseTime(scope.row.create_datetime) }}</span>
            </template>
          </el-table-column>
          <el-table-column
            v-if="hasPermi(['permission:user:{id}:put','permission:user:{id}:delete','permission:user:resetpwd:put'])"
            label="操作"
            align="center"
            width="160"
            class-name="small-padding fixed-width"
          >
            <template slot-scope="scope">
              <el-button
                v-hasPermi="['permission:user:{id}:put']"
                size="mini"
                type="text"
                icon="el-icon-edit"
                @click="handleUpdate(scope.row)"
              >修改
              </el-button>
              <el-button
                v-if="scope.row.id !== 1"
                v-hasPermi="['permission:user:{id}:delete']"
                size="mini"
                type="text"
                icon="el-icon-delete"
                @click="handleDelete(scope.row)"
              >删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>

        <pagination
          v-show="total>0"
          :total="total"
          :page.sync="queryParams.pageNum"
          :limit.sync="queryParams.pageSize"
          @pagination="getList"
        />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { listModule, listEfficiencyByParentId, listEfficiency } from "@/api/projects/efficiency";
import "@riophae/vue-treeselect/dist/vue-treeselect.css";

export default {
  name: "index",
  data() {
    return {
      // 遮罩层
      loading: true,
      // 选中数组
      ids: [],
      // 非单个禁用
      single: true,
      // 非多个禁用
      multiple: true,
      // 显示搜索条件
      showSearch: true,
      // 总条数
      total: 0,
      // 用户表格数据
      efficiencyList: null,
      // 弹出层标题
      title: "",
      moduleProps: undefined,
      // 模块树选项
      moduleOptions: undefined,
      // 是否显示弹出层
      open: false,
      // 模块名称
      moduleName: undefined,
      // 默认密码
      initPassword: undefined,
      // 日期范围
      dateRange: [],
      // 状态数据字典
      statusOptions: [{ dictLabel: "正常", dictValue: true }, { dictLabel: "停用", dictValue: false }],
      form: {},
      defaultProps: {
        children: "children",
        label: "label"
      },
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10,
        moduleName: undefined,
        is_active: undefined,
        moduleId: undefined,
        parentId: undefined,
      }
    };
  },
  watch: {
    // 根据名称筛选部门树
    moduleName(val) {
      this.$refs.tree.filter(val);
    }
  },
  created() {
    this.getList();
    this.getModuleTree();
    this.getDicts("sys_user_sex").then(response => {
      this.sexOptions = response.data;
    });
    this.getConfigKey("sys.user.initPassword").then(response => {
      this.initPassword = response.msg;
    });
  },
  methods: {
    /** 查询小工具列表 */
    getList() {
      this.loading = true;
      listEfficiency(this.addDateRange(this.queryParams, this.dateRange)).then(response => {
        this.efficiencyList = response.data.results;
        this.total = response.data.count;
        this.loading = false;
      }
      );
    },

    /** 查询模块下拉树结构 */
    getModuleTree() {
      listModule().then(response => {
        console.log(response)
        this.moduleOptions = this.handleTree(response.data.results, "id");
      });
    },
    // 筛选节点
    filterNode(value, data) {
      if (!value) return true;
      return data.label.indexOf(value) !== -1;
    },
    // 节点单击事件
    handleNodeClick(data) {
      this.queryParams.parentId = data.id;
      this.getList();
    },
    // 取消按钮
    cancel() {
      this.open = false;
      this.reset();
    },
    /** 搜索按钮操作 */
    handleQuery() {
      this.queryParams.page = 1;
      this.getList();
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.dateRange = [];
      this.queryParams.moduleId = "";
      this.resetForm("queryForm");
      this.handleQuery();
    },
    // 多选框选中数据
    handleSelectionChange(selection) {
      this.ids = selection.map(item => item.id);
      this.single = selection.length !== 1;
      this.multiple = !selection.length;
    },
  }
};
</script>
