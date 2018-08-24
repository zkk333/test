
kkuser_app_url1='http://test.kuaikuaikeji.com/kas/'
kkweight_app_url2='http://test.kuaikuaikeji.com/kcas/'
kk_user_app_url3='https://ts.kuaikuaikeji.com/kas/'
#kk_user_app_url4='https://ts1.kuaikuaikeji.com/kas/'
#kkweight_app_url2='http://stage.kuaikuaikeji.com/kcas/'
kk_zhiyun_url3='http://test.kuaikuaikeji.com/kims/'
快快减肥登录='ulogin'

获取用户称重信息='PadUserWeighingGetUserDataV2'
#print((url+a))
三次校验接口='PadGetUserCorrectWeightV2'
上传称重数据='PadUserWeighingUploadWeightDataV2'
快快教瘦登录='PadCoachLoginV2'
获取课程列表信息='PadGetCoachClassListV2'
获取课程列表信息私教='PadGetCoachClassInfoV2 '
开始课程='PadStartClassV2'
获取课程详细信息='PadGetCourseDetailV2'

获取课程详细信息私教='PadGetCourseDetailListV2'
查看签到状态='PadGetCoachClassCheckinV2'
上传报告='PadUploadAllClassDataV2'
报告列表='PadGetClassReportListV2'
体侧用户信息='PadGetUserInfoV2'
上传体侧数据接口='PadUploadPhysicalReportV2'
设置辅导员='PadSetCoachAssistantV2'
获取上课数据='http://kkuserdata.oss-cn-beijing.aliyuncs.com/bodydata/'
智运登录接口='AppLoginV2'
智运查询燃脂循环课学员信息接口='AppGetGymStdClassImportantUserListV2'
智运查询体验课学员接口='AppGetGymPreClassImportantUserListV2'
智运获取学员详细信息接口='AppGetUserDetailV2?random=8'
智运跟进记录接口='AppGetUserTraceListV2'
智运上传跟进记录接口='AppUploadUserTraceV2'
获取教练信息='AppGetGymCoachListV2'
获取销售人员信息='AppGetGymSaleListV2'
正式课购课时间='AppGetUserStdClassBuyListV2'
智运设置有效期='AppSetOrderExpireV2'
正式课预约时间='AppGetUserStdClassSubListV2'
正式课上课时间='AppGetUserStdClassTakeListV2'
称重记录='AppGetUserWeightListV2'
运动评估报告='AppGetUserReportListV2'
运动健康档案='AppGetUserPhysicalReportListV2'
学员备注='AppGetUserCommentListV2'
写备注='AppUploadUserCommentV2'
备注录入成功='AppGetUserCommentListV2'
运动规划报告接口='AppGetPlanningReportListV2'
私教课历史接口='AppGetUserClassListV2'
绩效接口='AppGetGymMoneyCommissionV2'
健康贡献接口='AppGetGymMoneyIncomeV2'
智运我的任务接口='AppGetTaskUserListV2'
获取我的任务里面的销售人员='AppGetCoachListV2'
店员指标排名='AppGetSaleGymDataV2'
具体店员指标月详情='AppGetSaleCoachDataV2'
具体店员指标日详情='AppGetMainDataMeDataV2?ranparam%20=%208'
报表='/AppDataProxyV2/dailyStat/statData'
今日课程='AppGetMainDataClassDataV2?ranparam%20=%203'
门店端='AppGetMainDataBossV2?ranparam%20=%208 '
app登录='ulogin'
商城购买='subjectqueryv9'#'subjectqueryv9
商城购买1='subjectqueryv9'
订单详情页='subjectorderdetail'
def 购课信息1(price_code):
    购课信息='getusablecouponcount?price_code={price_cede}&order_subject_number=1'.format(price_cede=price_code)
    return 购课信息
隐私协议='querydocs?type=storefront_protocol'
购买课程='ordersubjectv5'
def 购课成功1(order_uuid):
    购课成功='orderquey?order_uuid={order_uuid}'.format(order_uuid=order_uuid)
    return 购课成功
def 购课成功2(order_uuid):
    购课成功='paycheckv2?order_uuid={order_uuid}'.format(order_uuid=order_uuid)
    return 购课成功
我的课程='usersubjectlistv2?length=15 '
def 预约课程1(user_subject):
    预约课程='eleagreement?user_subject_uuid={user_subject}'.format(user_subject=user_subject)
    return 预约课程
def 城市列表1(subject_show_id):
    城市列表='openclasscitylist?subject_show_id={subject_show_id}'.format(subject_show_id=subject_show_id)
    return 城市列表
def 门店列表1(city,subject_show_id):
    门店列表='gymListNew?city={city}&subject_show_id={subject_show_id}&lat=39.905981&lon=116.640737'.format(city=city,subject_show_id=subject_show_id)
    return 门店列表
def 门店课程详细1(subject_show_id,gym_id):
   门店课程详细='classesList?subject_show_ids={subject_show_id}&gym_id={gym_id}'.format(subject_show_id=subject_show_id,gym_id=gym_id)
   return 门店课程详细
def 预约课程信息1(classes_id,user_subject_uuid):
   预约课程信息='queryclassesquota?user_subject_uuid={user_subject}&classes_id={classes_id}'.format(classes_id=classes_id,user_subject=user_subject_uuid)
   return  预约课程信息
预约成功='reserveclasses'
def 预约成功详情1(classes_id,user_subject_uuid):
   预约成功详情='classessubjectquery?classes_id={classes_id}&user_subject_uuid={user_subject}&query_type=1'.format(classes_id=classes_id,user_subject=user_subject_uuid)
   return  预约成功详情
发现='discoveryindexv4'
选择照片='stickerlist'
发布消息='fileupload'
发布成功='topicpublishv3'
发帖成功后='topiclistv4?circleID=0&length=12'