import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import ExamPaper from '../pages/exam/examPaper'
import Exam from '../pages/exam/exam'
import ExamList from '../pages/exam/examList'
import ExamRecord from '../pages/exam/examRecord'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import xinlizixunshiList from '../pages/xinlizixunshi/list'
import xinlizixunshiDetail from '../pages/xinlizixunshi/detail'
import xinlizixunshiAdd from '../pages/xinlizixunshi/add'
import yuyuezixunList from '../pages/yuyuezixun/list'
import yuyuezixunDetail from '../pages/yuyuezixun/detail'
import yuyuezixunAdd from '../pages/yuyuezixun/add'
import cepingjieguofenxiList from '../pages/cepingjieguofenxi/list'
import cepingjieguofenxiDetail from '../pages/cepingjieguofenxi/detail'
import cepingjieguofenxiAdd from '../pages/cepingjieguofenxi/add'
import zixunxiaoguopingguList from '../pages/zixunxiaoguopinggu/list'
import zixunxiaoguopingguDetail from '../pages/zixunxiaoguopinggu/detail'
import zixunxiaoguopingguAdd from '../pages/zixunxiaoguopinggu/add'
import fudaokechengList from '../pages/fudaokecheng/list'
import fudaokechengDetail from '../pages/fudaokecheng/detail'
import fudaokechengAdd from '../pages/fudaokecheng/add'
import fudaofanganList from '../pages/fudaofangan/list'
import fudaofanganDetail from '../pages/fudaofangan/detail'
import fudaofanganAdd from '../pages/fudaofangan/add'
import fudaojiluList from '../pages/fudaojilu/list'
import fudaojiluDetail from '../pages/fudaojilu/detail'
import fudaojiluAdd from '../pages/fudaojilu/add'
import fudaoxiaoguopingguList from '../pages/fudaoxiaoguopinggu/list'
import fudaoxiaoguopingguDetail from '../pages/fudaoxiaoguopinggu/detail'
import fudaoxiaoguopingguAdd from '../pages/fudaoxiaoguopinggu/add'
import shujutongjiList from '../pages/shujutongji/list'
import shujutongjiDetail from '../pages/shujutongji/detail'
import shujutongjiAdd from '../pages/shujutongji/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'examPaper',
					component: ExamPaper
				},
				{
					path: 'examList',
					component:ExamList
				},
				{
					path: 'examRecord/:type',
					component:ExamRecord
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'xinlizixunshi',
					component: xinlizixunshiList
				},
				{
					path: 'xinlizixunshiDetail',
					component: xinlizixunshiDetail
				},
				{
					path: 'xinlizixunshiAdd',
					component: xinlizixunshiAdd
				},
				{
					path: 'yuyuezixun',
					component: yuyuezixunList
				},
				{
					path: 'yuyuezixunDetail',
					component: yuyuezixunDetail
				},
				{
					path: 'yuyuezixunAdd',
					component: yuyuezixunAdd
				},
				{
					path: 'cepingjieguofenxi',
					component: cepingjieguofenxiList
				},
				{
					path: 'cepingjieguofenxiDetail',
					component: cepingjieguofenxiDetail
				},
				{
					path: 'cepingjieguofenxiAdd',
					component: cepingjieguofenxiAdd
				},
				{
					path: 'zixunxiaoguopinggu',
					component: zixunxiaoguopingguList
				},
				{
					path: 'zixunxiaoguopingguDetail',
					component: zixunxiaoguopingguDetail
				},
				{
					path: 'zixunxiaoguopingguAdd',
					component: zixunxiaoguopingguAdd
				},
				{
					path: 'fudaokecheng',
					component: fudaokechengList
				},
				{
					path: 'fudaokechengDetail',
					component: fudaokechengDetail
				},
				{
					path: 'fudaokechengAdd',
					component: fudaokechengAdd
				},
				{
					path: 'fudaofangan',
					component: fudaofanganList
				},
				{
					path: 'fudaofanganDetail',
					component: fudaofanganDetail
				},
				{
					path: 'fudaofanganAdd',
					component: fudaofanganAdd
				},
				{
					path: 'fudaojilu',
					component: fudaojiluList
				},
				{
					path: 'fudaojiluDetail',
					component: fudaojiluDetail
				},
				{
					path: 'fudaojiluAdd',
					component: fudaojiluAdd
				},
				{
					path: 'fudaoxiaoguopinggu',
					component: fudaoxiaoguopingguList
				},
				{
					path: 'fudaoxiaoguopingguDetail',
					component: fudaoxiaoguopingguDetail
				},
				{
					path: 'fudaoxiaoguopingguAdd',
					component: fudaoxiaoguopingguAdd
				},
				{
					path: 'shujutongji',
					component: shujutongjiList
				},
				{
					path: 'shujutongjiDetail',
					component: shujutongjiDetail
				},
				{
					path: 'shujutongjiAdd',
					component: shujutongjiAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
		{
			path: '/exam',
			component: Exam
		}
	]
})
