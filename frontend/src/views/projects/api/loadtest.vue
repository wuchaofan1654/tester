<template> 
  <div class="app-container">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-collapse v-model="activeNames" @change="handleChange">
          <el-collapse-item title="压测服务器配置" name="1">
            <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="80" class="demo-dynamic">
              <el-form-item prop="email" label="master">
                <el-row :gutter="22">
                  <el-col :span="14">
                    <el-input size="mini" v-model="dynamicValidateForm.email"></el-input>
                  </el-col>
                  <el-col :span="4">
                    <el-button type="text" icon="el-icon-plus" @click.prevent="addDomain(domain)"></el-button>
                  </el-col>
                </el-row>
              </el-form-item>
              <el-form-item
                v-for="(domain, index) in dynamicValidateForm.domains"
                :label="'slave' + (index + 1)"
                :key="domain.key"
                :prop="'domains.' + index + '.value'">
                <el-row :gutter="22">
                  <el-col :span="14">
                    <el-input v-model="domain.value" size="mini"></el-input>
                  </el-col>
                  <el-col :span="4">
                    <el-button type="text" icon="el-icon-delete" @click.prevent="removeDomain(domain)"></el-button>
                  </el-col>
                </el-row>
              </el-form-item>
              <el-form-item>
                <el-button size="mini" type="primary" @click="submitForm('dynamicValidateForm')">提交</el-button>
                <el-button size="mini" @click="addDomain">新增slave</el-button>
                <el-button size="mini" @click="resetForm('dynamicValidateForm')">重置</el-button>
              </el-form-item>
            </el-form>
          </el-collapse-item>
          <el-collapse-item title="全局参数配置" name="2">
            <div>控制反馈：通过界面样式和交互动效让用户可以清晰的感知自己的操作；</div>
            <div>页面反馈：操作后，通过页面元素的变化清晰地展现当前状态。</div>
          </el-collapse-item>
          <el-collapse-item title="csv文件参数配置" name="3">
            <div>简化流程：设计简洁直观的操作流程；</div>
            <div>清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；</div>
            <div>帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。</div>
          </el-collapse-item>
          <el-collapse-item title="报告配置" name="4">
            <div>用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
            <div>结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
          </el-collapse-item>
        </el-collapse>
      </el-col>
      <el-col :span="16">
        <el-table v-loading="loading" :data="apiList" @selection-change="handleSelectionChange">
          <el-table-column type="selection" width="55" align="center" />
          <el-table-column label="编号" prop="id" width="80" />
          <el-table-column label="接口名称" prop="name" :show-overflow-tooltip="true" />
          <el-table-column label="请求url" prop="url" :show-overflow-tooltip="true" />
          <el-table-column label="权重" prop="weight" width="100" :show-overflow-tooltip="true" />
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
      </el-col>
    </el-row>
  </div>
</template>
<script>
import {listApi} from '@/api/projects/api'

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
      dynamicValidateForm: {
          domains: [{
            value: ''
          }],
          email: ''
        },
      apiList: [],
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
      listApi(this.queryParams).then(response => {
        this.loading = false;
        this.apiList = response.data.results;
        this.total = response.data.count
      });
    },
    /** 搜索按钮点击 */
    handleQuery() {
      this.getList()
    },
    pTypeFormat(row, column) {
      return row.key_yn === 1 ? '事件': '页面'
    },
    // 埋点是否核心字典翻译
    keyYnFormat(row, column) {
      return row.key_yn === 1 ? '是': '否'
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
    handleSelectionChange(){},
    submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      removeDomain(item) {
        let index = this.dynamicValidateForm.domains.indexOf(item)
        if (index !== -1) {
          this.dynamicValidateForm.domains.splice(index, 1)
        }
      },
      addDomain() {
        this.dynamicValidateForm.domains.push({
          value: '',
          key: Date.now()
        });
      }
  }
}
</script>
<style></style>


