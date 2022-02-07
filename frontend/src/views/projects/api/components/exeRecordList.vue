<template>
  <div class="app-container">
    <span><i class="el-icon-timer">历史查询记录</i></span>
    <el-button class="clear-bnt" type="text" icon="el-icon-delete">清空</el-button>
    <div v-for="(record, index) in records">
      <el-button class="el-rec-link" type="text" @click="exeRpc(mergeQueryParams(record))">
        {{index + 1}}.<span v-for="item in record.items">{{item.item_name}}.</span>
      </el-button>
      <p class="p-create-time"><i class="el-icon-time"> {{record.create_datetime}}</i></p>
    </div>
  </div>
</template>

<script>
import {getRpcRecords, executeRpc} from "@/api/projects/api";

export default {
  name: "exeRecordList",
  props: ['evn'],
  data() {
    return {
      records: [],
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList(){
      getRpcRecords().then(response => {
        if (response.code === 200) {
          this.records = response.data.results
        } else {
          this.records = []
        }
      })
    },
    mergeQueryParams(record) {
      return {
        evn: this.evn,
        items: record.items,
        params: record.params
      }
    },
    exeRpc(params) {
      let result
      executeRpc(params).then(response => {
        if (response.code === 200) {
          result = response.data
        } else {
          result = response
        }
        this.$emit('getExeResult', result)
      })
    }
  },
}
</script>

<style scoped>
.clear-bnt {
  padding-left: 10px;
}
.el-rec-link{
  font-size: 12px;
}
.p-create-time {
  font-size: 8px;
  color: gray
}

</style>
