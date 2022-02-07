<template>
  <div class="app-container home">
    <el-row :gutter="20">
      <el-col :sm="24" :lg="12" style="padding-left: 20px">
        <h1>Tester平台</h1>
        <p>
          一直想做一款后台管理系统，看了很多优秀的开源项目，发现只有Java、Go，但是发现没有合适Python的。于是利用空闲休息时间开始自己写一
          套后台系统。如此有了Tester平台。您可以基于此系统进行持续开发，以做出符合自己系统。所有前端后台代码封装过后十分精简易上手，
          出错概率低。同时支持移动客户端访问。系统会陆续更新一些实用功能。
        </p>
        <p>
          <b>当前版本:</b> <span>v{{ version }}</span>
        </p>
      </el-col>

      <el-col :sm="24" :lg="12" style="padding-left: 50px">
        <el-row>
          <el-col :span="12">
            <h1>技术选型</h1>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="8">
            <h4>后端技术</h4>
            <ul>
              <li>Django</li>
              <li>django-redis</li>
              <li>django-celery-beat</li>
              <li>django-rest-framework</li>
              <li>django-rest-framework-jwt</li>
              <li>...</li>
            </ul>
          </el-col>
          <el-col :span="8">
            <h4>前端技术</h4>
            <ul>
              <li>Vuex</li>
              <li>Element-ui</li>
              <li>Axios</li>
              <li>Sass</li>
              <li>Quill</li>
              <li>...</li>
            </ul>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
    <el-divider />
  </div>
</template>

<script>
export default {
  name: "Index",
  data() {
    return {
      // 版本号
      version: "1.1.1"
    };
  },
  methods: {}
};
</script>

<style scoped lang="scss">
  .home {
    blockquote {
      padding: 10px 20px;
      margin: 0 0 20px;
      font-size: 17.5px;
      border-left: 5px solid #eee;
    }

    hr {
      margin-top: 20px;
      margin-bottom: 20px;
      border: 0;
      border-top: 1px solid #eee;
    }

    .col-item {
      margin-bottom: 20px;
    }

    ul {
      padding: 0;
      margin: 0;
    }

    font-family: "open sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 13px;
    color: #676a6c;
    overflow-x: hidden;

    ul {
      list-style-type: none;
    }

    h4 {
      margin-top: 0;
    }

    h2 {
      margin-top: 10px;
      font-size: 26px;
      font-weight: 100;
    }

    p {
      margin-top: 10px;

      b {
        font-weight: 700;
      }
    }

    .update-log {
      ol {
        display: block;
        list-style-type: decimal;
        margin-block-start: 1em;
        margin-block-end: 1em;
        margin-inline-start: 0;
        margin-inline-end: 0;
        padding-inline-start: 40px;
      }
    }
  }
</style>

