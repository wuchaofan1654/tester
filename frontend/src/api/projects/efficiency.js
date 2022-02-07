import request from "@/utils/request";

// 查询模块列表
export function listModule(query) {
  return request({
    url: "/pro/efficiency/module",
    method: "get",
    params: query
  });
}

// 查询模块列表
export function listModuleTree(query) {
  return request({
    url: "/pro/efficiency/module",
    method: "get",
    params: query
  });
}

// 查询小工具列表
export function listEfficiency(query) {
  return request({
    url: "/pro/efficiency/efficiency",
    method: "get",
    params: query
  });
}
