import request from "@/utils/request";

// 查询接口集列表
export function listApiSuite(query) {
  return request({
    url: "/pro/api/suite/",
    method: "get",
    params: query
  });
}

// 查询接口集详细
export function getApiSuite(suiteId) {
  return request({
    url: "/pro/api/suite/" + suiteId,
    method: "get"
  });
}

// 新增接口集
export function addApiSuite(data) {
  return request({
    url: "/pro/api/suite/",
    method: "post",
    data: data
  });
}

// 修改接口集
export function updateApiSuite(data) {
  return request({
    url: "/pro/api/suite/",
    method: "put",
    data: data
  });
}

// 删除接口集
export function deleteApiSuite(suiteId) {
  return request({
    url: "/pro/api/suite/" + suiteId + "/",
    method: "delete"
  });
}


// 查询接口集列表
export function listApi(query) {
  return request({
    url: "/pro/api/api/",
    method: "get",
    params: query
  });
}

// 查询接口集详细
export function getApi(apiId) {
  return request({
    url: "/pro/api/api/" + apiId,
    method: "get"
  });
}

// 新增接口集
export function addApi(data) {
  return request({
    url: "/pro/api/api/",
    method: "post",
    data: data
  });
}

// 修改接口集
export function updateApi(data) {
  return request({
    url: "/pro/api/api/",
    method: "put",
    data: data
  });
}

// 删除接口集
export function deleteApi(apiId) {
  return request({
    url: "/pro/api/api/" + apiId + "/",
    method: "delete"
  });
}


export function getRpcItems(parentId) {
  if (parentId === 'undefined' || !parentId) {
    parentId = ''
  }
  return request({
      url: "/pro/api/rpc/p" + parentId + "/",
      method: "get"
    });
}


export function getRpcRecords() {
  return request({
      url: "/pro/api/rpc/records/",
      method: "get"
    });
}


export function executeRpc(data) {
  return request(
    {
      url: '/pro/api/rpc/execute/',
      method: "post",
      data: data
    }
  )
}
