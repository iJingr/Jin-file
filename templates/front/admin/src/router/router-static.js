import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
import adminexam from '@/views/modules/exampaperlist/exam'
    import news from '@/views/modules/news/list'
    import cepingjieguofenxi from '@/views/modules/cepingjieguofenxi/list'
    import examquestion from '@/views/modules/examquestion/list'
    import exampaper from '@/views/modules/exampaper/list'
    import xinlizixunshi from '@/views/modules/xinlizixunshi/list'
    import zixunxiaoguopinggu from '@/views/modules/zixunxiaoguopinggu/list'
    import fudaofangan from '@/views/modules/fudaofangan/list'
    import fudaoxiaoguopinggu from '@/views/modules/fudaoxiaoguopinggu/list'
    import shujutongji from '@/views/modules/shujutongji/list'
    import yuyuezixun from '@/views/modules/yuyuezixun/list'
    import yonghu from '@/views/modules/yonghu/list'
    import exampaperlist from '@/views/modules/exampaperlist/list'
    import fudaokecheng from '@/views/modules/fudaokecheng/list'
    import fudaojilu from '@/views/modules/fudaojilu/list'
    import config from '@/views/modules/config/list'
    import examrecord from '@/views/modules/examrecord/list'
    import newstype from '@/views/modules/newstype/list'


//2.配置路由   注意：名字
export const routes = [{
    path: '/',
    name: '系统首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '系统首页',
      component: Home,
      meta: {icon:'', title:'center', affix: true}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/news',
        name: '通知公告',
        component: news
      }
      ,{
	path: '/cepingjieguofenxi',
        name: '测评结果分析',
        component: cepingjieguofenxi
      }
      ,{
	path: '/examquestion',
        name: '测试试题管理',
        component: examquestion
      }
      ,{
	path: '/exampaper',
        name: '心理测评管理',
        component: exampaper
      }
      ,{
	path: '/xinlizixunshi',
        name: '心理咨询师',
        component: xinlizixunshi
      }
      ,{
	path: '/zixunxiaoguopinggu',
        name: '咨询效果评估',
        component: zixunxiaoguopinggu
      }
      ,{
	path: '/fudaofangan',
        name: '辅导方案',
        component: fudaofangan
      }
      ,{
	path: '/fudaoxiaoguopinggu',
        name: '辅导效果评估',
        component: fudaoxiaoguopinggu
      }
      ,{
	path: '/shujutongji',
        name: '数据统计',
        component: shujutongji
      }
      ,{
	path: '/yuyuezixun',
        name: '预约咨询',
        component: yuyuezixun
      }
      ,{
	path: '/yonghu',
        name: '用户',
        component: yonghu
      }
      ,{
	path: '/exampaperlist',
        name: '心理测评列表',
        component: exampaperlist
      }
      ,{
	path: '/fudaokecheng',
        name: '辅导课程',
        component: fudaokecheng
      }
      ,{
	path: '/fudaojilu',
        name: '辅导记录',
        component: fudaojilu
      }
      ,{
	path: '/config',
        name: '轮播图管理',
        component: config
      }
      ,{
	path: '/examrecord',
        name: '心理测试记录',
        component: examrecord
      }
      ,{
	path: '/newstype',
        name: '通知公告分类',
        component: newstype
      }
    ]
  },
  {
    path: '/adminexam',
    name: 'adminexam',
    component: adminexam,
    meta: {icon:'', title:'adminexam'}
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'hash',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
}
export default router;
