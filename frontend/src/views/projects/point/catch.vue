<template>
  <div class="app-container">
    <el-card>
      <div slot="header" class="clearfix">
        <span class="color-info"><i class="el-icon-timer">【实时埋点】</i></span>
        <el-button type="text" @click="changeWebsocketStatus">
          <span :class="socketInfo.color"><i class="el-icon-video-camera-solid"> {{ socketInfo.text }}</i></span>
        </el-button>
        <div style="float: right; padding: 3px 0">
          <span class="class-filter-option">CURRENT IP:</span>
          <span style="color: #451c22">{{currentIp}}</span>
          <span class="class-filter-option">埋点类型:</span>
          <el-select placeholder="请选择过滤类型" clearable size="mini" v-model="filters.pType">
            <el-option v-for="item in typeOptions" :key="item.value" :label="item.label" :value="item.value">
              <span style="float: left">{{ item.label }}</span>
              <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
            </el-option>
          </el-select>
          <span class="class-filter-option">监听环境:</span>
          <el-select placeholder="域名" size="mini" v-model="filters.host">
            <el-option v-for="item in properties.hosts" :key="item.value" :label="item.label" :value="item.value">
              <span style="float: left">{{ item.label }}</span>
              <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
            </el-option>
          </el-select>
          <span class="class-filter-option">端口:</span>
          <el-input size="mini" v-model="properties.port" placeholder="默认9999" style="width: 100px"></el-input>
        </div>
      </div>
      <el-row :gutter="22">
        <el-col :span="6">
          <div class="left-side">
            <el-input size="mini" v-model="filters.name" prefix-icon="el-icon-search"
                      placeholder="支持埋点名称过滤">
              <el-button slot="append" icon="el-icon-delete" @click=""></el-button>
            </el-input>
            <p v-if="points.length === 0" class="color-info" style="padding-top: 10px; font-size: 12px">
              <el-empty :image-size="50" description="请先开始录制"></el-empty>
            </p>
            <div v-else class="point-name-list" v-for="point in points" :key="getPointName(point)" @click="tapPointName(point)">
              <el-link v-if="getPointName(point)" type="success" icon="el-icon-success" :underline="false">
                {{ getPointName(point) }}
              </el-link>
            </div>
          </div>
        </el-col>
        <el-col :span="18">
          <div class="right-side">
            <div style="float: right; font-size: 13px">
              <span class="color-info"><i class="el-icon-document"> 当前选中埋点详情</i></span>
              <el-button type="text" icon="el-icon-refresh" @click="changeFormat"> {{ properties.format.text }}</el-button>
            </div>
            <span class="result-tags" v-for="result in results" :key="result.message">
              <el-tag :type='mapResultStatus(result.status)' size="mini">
                {{ result.message }}
              </el-tag>
            </span>
            <json-viewer
              v-if="selectedPoint.type"
              :value="simplePoint(selectedPoint)"
              :expand-depth="5"
              sort></json-viewer>
            <p v-else class="color-info" style="padding-top: 10px; font-size: 12px">
              <el-empty :image-size="100" description="当前未选中埋点"></el-empty>
            </p>
          </div>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>

import store from "@/store";


export default {
  data() {
    return {
      currentIp: document.location.hostname,
      filters: {},
      properties: {
        port: '',
        format: { simpleYn: false, text: '详细样式'},
        hosts: [{label: '测试', value: 'testst3'}, {label: '线上', value: 'st3'}]
      },
      socketInfo: {
        websocketTurnOn: false,
        text: '开始录制',
        color: 'color-primary'
      },
      typeOptions: [{label: '事件埋点', value: 1}, {label: '页面埋点', value: 2}],
      selectedPoint: {},
      results: [],  // {message: '', status: 1}
      points: [],
    }
  },
  methods: {
    initWebSocket() {
      let device = store.getters.device
      const wsuri =
        "ws://127.0.0.1:8088"
        + "/ws/points/catch/"
        + device + "/"

      this.websocket = new WebSocket(wsuri);
      this.websocket.onopen = this.websocketonopen;
      this.websocket.onerror = this.websocketonerror;
      this.websocket.onmessage = this.websocketonmessage;
      this.websocket.onclose = this.websocketclose;
    },
    closeWebsocket() {
      this.websocket.close()
    },
    websocketonopen() {
      this.$message.success('websocket通信启动成功～')
    },
    websocketonerror(e) {
      this.$message.error('websocket发生错误～')
    },
    websocketonmessage(e) {
      let data = JSON.parse(e.data).message;
      if (this.filters.pType && this.filters.pType !== data.type) {
        return
      }
      if (this.filters.name && this.getPointName(data).search(this.filters.name) === -1) {
        return
      }
      this.points.unshift(data)
    },
    websocketclose(e) {
      this.$message.info('websocket通信已关闭～')
      this.socketInfo.websocketTurnOn = false
      this.socketInfo.text = '开始录制'
      this.socketInfo.color = 'color-primary'
    },
    filterPoints(point) {
      return point.name === this.filters.type;
    },
    getPointName(point) {
      return point.type === 1 ? point.from_action : point.curr_page
    },
    mapResultStatus(status) {
      return status === 1 ? 'success' : status === 2 ? 'warning' : status === 3 ? 'danger' : 'info'
    },
    changeFormat() {
      this.properties.format.simpleYn = !this.properties.format.simpleYn
      this.properties.format.text = this.properties.format.simpleYn ? '精简样式' : '详细样式'
    },
    changeWebsocketStatus() {
      this.socketInfo.websocketTurnOn = !this.socketInfo.websocketTurnOn
      if (this.socketInfo.websocketTurnOn) {
        this.socketInfo.text = '停止录制'
        this.socketInfo.color = 'color-danger'
        this.initWebSocket()
      } else {
        this.socketInfo.text = '开始录制'
        this.socketInfo.color = 'color-primary'
        this.closeWebsocket()
      }
    },
    tapPointName(point) {
      this.selectedPoint = point
      this.fetchPointCheckResult()
    },
    fetchPointCheckResult() {
      // todo
    },
    resetPoints() {
      this.selectedPoint = {}
      this.points = []
      this.results = {}
    },
    simplePoint(point) {
      if (!point) {
        return {}
      } else if (!this.properties.format.simpleYn) {
        return point
      } else {
        return {
          type: point.type,
          from_page: point.from_page,
          curr_page: point.curr_page,
          curr_page_ext: point.curr_page_ext,
          from_action: point.from_action,
          from_action_ext: point.from_action_ext
        }
      }
    }
  },
}
</script>
<style slot-scope="scope">
.left-side {
  min-height: 600px;
  overflow: scroll;
  border-right:  1px solid #e7e6e6;
}
.right-side {
  min-height: 600px;
  overflow: scroll;
}
.result-tags {
  padding: 0 0 0 10px;
}
.point-name-list {
  word-break: break-all;
  padding-bottom: 5px;
  padding-top: 5px;
}
.class-filter-option {
  padding-left: 20px;
  padding-right: 5px;
  font-size: 13px;
  color: gray;
  font-weight: bolder;
}
</style>
