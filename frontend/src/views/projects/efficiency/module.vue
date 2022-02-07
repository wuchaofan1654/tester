<template>
  <div class="app-container" style="width: 60%">
    <el-form ref="queryForm" :model="queryParams" :inline="true">
      <el-form-item label="菜单名称" prop="name">
        <el-input
          v-model="queryParams.name"
          placeholder="请输入菜单名称"
          clearable
          size="small"
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>
    <el-table
      v-loading="loading"
      :data="moduleList"
      row-key="id"
      :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
      <el-table-column prop="name" label="模块名称" :show-overflow-tooltip="true" width="160" />
      <el-table-column prop="orderNum" label="排序" width="60" />
      <el-table-column prop="status" label="状态" width="80" />
      <el-table-column label="创建时间" align="center" prop="create_datetime">
        <template slot-scope="scope">
          <span>{{ parseTime(scope.row.create_datetime) }}</span>
        </template>
      </el-table-column>
      <el-table-column
        v-if="hasPermi(['permission:menus:{id}:put', 'permission:menus:post', 'permission:menus:{id}:delete'])"
        label="操作"
        align="center"
        class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button
            v-hasPermi="['permission:menus:{id}:put']"
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"
          >修改
          </el-button>
          <el-button
            v-hasPermi="['permission:menus:post']"
            size="mini"
            type="text"
            icon="el-icon-plus"
            @click="handleAdd(scope.row)"
          >新增
          </el-button>
          <el-button
            v-hasPermi="['permission:menus:{id}:delete']"
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click=""
          >删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { listModule } from "@/api/projects/efficiency";
import Treeselect from "@riophae/vue-treeselect";
import "@riophae/vue-treeselect/dist/vue-treeselect.css";
import IconSelect from "@/components/IconSelect";

export default {
  name: "Module",
  components: { Treeselect, IconSelect },
  data() {
    return {
      // 遮罩层
      loading: true,
      // 模块表格树数据
      moduleList: [],
      // 弹出层标题
      title: "",
      // 是否显示弹出层
      open: false,
      // 显示状态数据字典
      queryParams: {
        name: undefined,
        pageNum: "all"
      },
      form: {},
    };
  },
  created() {
    this.getList();
    this.getDicts("sys_show_hide").then(response => {
      this.visibleOptions = response.data;
    });
    this.getDicts("sys_normal_disable").then(response => {
      this.statusOptions = response.data;
    });
    this.getDicts("sys_menu_type").then(response => {
      this.menuTypeOptions = response.data;
    });
    this.getDicts("sys_interface_method").then(response => {
      this.interfaceMethodOptions = response.data;
    });
  },
  methods: {
    getList() {
      this.loading = true;
      listModule(this.queryParams).then(response => {
        console.log(response.data)
        this.moduleList = this.handleTree(response.data, "id");
        console.log(this.moduleList)
        this.loading = false;
      });
    },
    reset() {
      this.form = {
        id: undefined,
        parentId: 0,
        name: undefined
      };
      this.resetForm("form");
    },
    /** 搜索按钮操作 */
    handleQuery() {
      this.getList();
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.resetForm("queryForm");
      this.handleQuery();
    },
    /** 新增按钮操作 */
    handleAdd(row) {
      this.reset();
      this.getTreeselect();
      if (row != null && row.id) {
        this.form.parentId = row.id;
      } else {
        this.form.parentId = 0;
      }
      this.open = true;
      this.title = "添加菜单";
    },
    /** 修改按钮操作 */
    handleUpdate(row) {
      this.reset();
      this.getTreeselect();
      getMenu(row.id).then(response => {
        this.form = response.data;
        this.open = true;
        this.title = "修改菜单";
      });
    },
  }
};
</script>
