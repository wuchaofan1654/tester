import request from "@/utils/request";

// 查询埋点列表
export function listPoint(query) {
  return request({
    url: "/pro/point/point/",
    method: "get",
    params: query
  });
}

// 查询埋点详细
export function getPoint(menuId) {
  return request({
    url: "/pro/point/point/" + menuId,
    method: "get"
  });
}

// 新增埋点
export function addPoint(data) {
  return request({
    url: "/pro/point/point/",
    method: "post",
    data: data
  });
}

// 修改埋点
export function updatePoint(data) {
  return request({
    url: "/pro/point/point/" + data.id + "/",
    method: "put",
    data: data
  });
}

// 删除菜单
export function delPoint(pointId) {
  return request({
    url: "/pro/point/point/" + pointId + "/",
    method: "delete"
  });
}

// 查询埋点列表
export function listPointSuite(query) {
  return request({
    url: "/pro/point/suite",
    method: "get",
    params: query
  });
}
