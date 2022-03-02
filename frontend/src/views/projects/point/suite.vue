<template> 
  <div style="margin: 20px 10px 20px 10px">
    <el-form v-show="showSearch" ref="queryForm" :model="queryParams" :inline="true">
      <el-form-item label="埋点集合名称" prop="name">
        <el-input
          v-model="queryParams.name"
          placeholder="请输入埋点集合名称"
          clearable
          size="small"
          style="width: 240px"
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="负责人" prop="owner">
        <el-input
          v-model="queryParams.owner"
          placeholder="请输入负责人名"
          clearable
          size="small"
          style="width: 240px"
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="创建时间">
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

    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
          v-hasPermi="['permission:role:post']"
          type="primary"
          plain
          icon="el-icon-plus"
          size="mini"
          @click="handleAdd"
        >新增</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          v-hasPermi="['permission:role:{id}:put']"
          type="success"
          plain
          icon="el-icon-edit"
          size="mini"
          :disabled="single"
          @click="handleUpdate"
        >修改</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          v-hasPermi="['permission:role:{id}:delete']"
          type="danger"
          plain
          icon="el-icon-delete"
          size="mini"
          :disabled="multiple"
          @click="handleDelete"
        >删除</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          v-hasPermi="['permission:role:export:get']"
          type="warning"
          plain
          icon="el-icon-download"
          size="mini"
          @click="handleExport"
        >导出</el-button>
      </el-col>
      <right-toolbar :show-search.sync="showSearch" @queryTable="getList" />
    </el-row>

    <el-table v-loading="loading" :data="suiteList" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55" align="center" />
      <el-table-column label="埋点编号" prop="id" width="80" />
      <el-table-column label="集合名称" prop="name" :show-overflow-tooltip="true" />
      <el-table-column label="所属团队" prop="dept" :show-overflow-tooltip="true" />
      <el-table-column label="埋点数量" prop="points" width="100" />
      <el-table-column label="状态" align="center" width="100" sortable>
        <template slot-scope="scope">
          <el-switch
            v-model="scope.row.status.toString()"
            active-value="1"
            inactive-value="0"
            disabled
            @change="handleStatusChange(scope.row)"
          />
        </template>
      </el-table-column>
      <el-table-column label="创建时间" align="center" prop="create_datetime">
        <template slot-scope="scope">
          <span>{{ parseTime(scope.row.create_datetime) }}</span>
        </template>
      </el-table-column>
      <el-table-column
        v-if="hasPermi(['permission:role:{id}:put', 'permission:role:{id}:delete'])"
        label="操作"
        align="center"
        class-name="small-padding fixed-width"
      >
        <template slot-scope="scope">
          <el-button
            v-hasPermi="['permission:role:{id}:put']"
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"
          >修改</el-button>
          <el-button
            v-hasPermi="['permission:role:{id}:put']"
            size="mini"
            type="text"
            icon="el-icon-circle-check"
            @click="handleDataScope(scope.row)"
          >数据权限</el-button>
          <el-button
            v-hasPermi="['permission:role:{id}:delete']"
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)"
          >删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
import {listPointSuite} from '@/api/projects/point'

const defaultQueryParams = {
  name: null,
  owner: null,
  key_yn: null,
  status: null,
  pageNum: 1,
  pageSize: 20
};

export default {
  name: "points",
  data() {
    return {
      suiteList: [],
      showSearch: true,
      single: true,
      // 非多个禁用
      multiple: true,
      dateRange: null,
      statusOptions: [],
      queryParams: Object.assign({}, defaultQueryParams),
      loading: true,
    }
  },
  created() {
    this.getList();
  },
  methods: {
    getList() {
      this.loading = true;
      listPointSuite(this.queryParams).then(response => {
        this.loading = false;
        this.suiteList = response.data.results;
        this.total = response.data.count
      });
    },
    /** 搜索按钮点击 */
    handleQuery() {
      this.getList()
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.dateRange = [];
      this.resetForm("queryForm");
      this.handleQuery();
    },
    handleSizeChange(val) {
      this.queryParams.pageNum = 1;
      this.queryParams.pageSize = val;
      this.getList();
    },
    handleCurrentChange(val) {
      this.queryParams.pageNum = val;
      this.getList();
    },
    handleStatusChange() {
      this.$router.push({path:'/apis/addApi'});
    },
    handleAdd() {

    },
    handleDelete() {

    },
    handleUpdate() {},
    handleDataScope(){},
    handleExport() {},
    handleSelectionChange(){}

  }
}
</script>
<style></style>


