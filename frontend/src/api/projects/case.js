import request from "@/utils/request";

// 查询接口集列表
export function listModule(query) {
  return request({
    url: "/pro/case/module/",
    method: "get",
    params: query
  });
}

// 查询接口集详细
export function getModule(suiteId) {
  return request({
    url: "/pro/api/suite/" + suiteId,
    method: "get"
  });
}

// 新增接口集
export function addModule(data) {
  return request({
    url: "/pro/api/suite/",
    method: "post",
    data: data
  });
}

// 修改接口集
export function updateModule(data) {
  return request({
    url: "/pro/api/suite/",
    method: "put",
    data: data
  });
}

// 删除接口集
export function deleteModule(suiteId) {
  return request({
    url: "/pro/api/suite/" + suiteId + "/",
    method: "delete"
  });
}


// 查询接口集列表
export function listCase(query) {
  return request({
    url: "/pro/case/case/",
    method: "get",
    params: query
  });
}

// 查询接口集详细
export function getCase(caseId) {
  return request({
    url: "/pro/case/case/" + caseId,
    method: "get"
  });
}

// 新增接口集
export function addCase(data) {
  return request({
    url: "/pro/case/case/",
    method: "post",
    data: data
  });
}

// 修改接口集
export function updateCase(data) {
  return request({
    url: "/pro/case/case/",
    method: "put",
    data: data
  });
}

// 删除接口集
export function deleteCase(caseId) {
  return request({
    url: "/pro/case/case/" + caseId + "/",
    method: "delete"
  });
}

// 查询接口集列表
export function listCaseSuite(query) {
  return request({
    url: "/pro/case/suite/",
    method: "get",
    params: query
  });
}

// 查询接口集详细
export function getCaseSuite(suiteId) {
  return request({
    url: "/pro/case/suite/" + suiteId,
    method: "get"
  });
}

// 新增接口集
export function addCaseSuite(data) {
  return request({
    url: "/pro/case/suite/",
    method: "post",
    data: data
  });
}

// 修改接口集
export function updateCaseSuite(data) {
  return request({
    url: "/pro/case/suite/",
    method: "put",
    data: data
  });
}

// 删除接口集
export function deleteCaseSuite(suiteId) {
  return request({
    url: "/pro/case/suite/" + suiteId + "/",
    method: "delete"
  });
}

