<template> 
  <div class="app-container">
    <div class="header-banner">
      <el-image class="img-banner" src="" fit="fill" />
    </div>
    <el-row :gutter="22">
      <el-col :span="16">
      <div class="main-content">
        <el-form :model="formData" label-width="100px" class="demo-ruleForm">
          <el-form-item label="运行环境" prop="env">
            <el-radio-group v-model="formData.env">
              <el-radio v-for="evn in evnOptions" :label="evn.host">{{evn.name}}</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="选择rpc服务" prop="rpcs">
            <rpc-cas @getSelectedItems="updateSelectedItems" style="width: 80%"></rpc-cas>
          </el-form-item>
          <el-form-item label="请求参数" prop="params">
            <el-input
              style="width: 80%"
              type="textarea"
              placeholder='请填写参数信息：json格式'
              :autosize="{minRows:5, maxRows:20}"
              v-model="formData.params"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="success" @click="submitForm">执行并保存</el-button>
          </el-form-item>
        </el-form>
        <div v-if="result">
          <p class="color-gray"><i class="el-icon-chat-dot-square"> 输出结果信息</i></p>
          <pre style="padding-left: 10px">{{result}}</pre>
        </div>
      </div>
    </el-col>
      <el-col :span="8">
        <exe-list @getExeResult="updateResult" :evn="this.formData.env" ref="exeRecordList"></exe-list>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import rpcCascader from "@/views/projects/api/components/rpcCascader";
import exeRecordList from "@/views/projects/api/components/exeRecordList";

export default {
  components: {
    'rpc-cas': rpcCascader,
    'exe-list': exeRecordList
  },
  data() {
    return {
      result: '',
      visible: false,
      formData: {
        env: 'http://api8.soyoung.com',
        items: [],
        params: '',
      },
      evnOptions: [
        {host: 'http://api.sy.soyoung.com', name: '测试环境'},
        {host: 'http://api8.soyoung.com', name: '预发布环境'},
        {host: 'http://api.soyoung.com', name: '生产环境'},
      ]
    };
  },
  created() {
    this.updateSelectedItems()
  },
  methods: {
    updateSelectedItems(node) {
      if (!node) {
        return
      }
      console.log(node)
      let ids = node.path
      let labels = node.pathLabels
      let len = ids.length;
      for (let i=0; i < len; i++){
        let item = {};
        item.id = ids[i];
        item.item_name = labels[i];
        this.formData.items.push(item);
      }
    },
    updateResult(data) {
      this.visible = true
      this.result = data
    },
    submitForm() {
      this.visible = true
      if (this.formData.items.length > 1) {
        this.result = this.$refs.exeRecordList.exeRpc(this.formData)
      } else {
        this.$message.error('请选择rpc服务及方法')
      }
    },
    resetForm() {
      this.resetFields();
    }
  }
}
</script>

<style>
  .main-content {
    padding-top: 20px;
    padding-left: 20px;
  }
  .img-banner {
    width: 100%;
    height: 100%;
  }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }
</style>
