const base = {
    get() {
        return {
            url : "http://localhost:8080/django5hdklc84/",
            name: "django5hdklc84",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "高校心理测评与辅导管理系统"
        } 
    }
}
export default base
