# 作者：SN-Grotesque（Author: SN-Grotesque）
import requests

x=0
while True:
    url_tdjl = "https://jobs.mihoyo.com/api/apply/mihoyo/612ec466-7d0e-42dc-b489-f460ff282a38"  # 投递网址
    h = {
        "Host": "jobs.mihoyo.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"
    }  # 请求头部

    website = x  # 个人网站 - 没有就写 无
    name = x  # 姓名
    gender = x  # 性别
    phone = x  # 手机号 - 不需要+86
    email = x  # 电子邮箱
    birthdate = x  # 出生日期 - 格式 1970-01-01
    location = x  # 所在地
    academicDegree = x  # 学历
    graduateDate = x  # 毕业到开始找工作的时间  - 只写年月
    startFrom = x  # 到岗时间 - 不是几月几日，如“随时到岗”
    salary = x  # 当前薪资
    aimSalary = x  # 期望薪资
    startDate = x  # 开始工作的时间  - 只写年月
    endDate = x  # 结束工作的时间  - 只写年月 - 未离职填 至今
    company = x  # 公司名称
    title = x  # 职位名称
    location_gs = x  # 公司地址
    industry = x  # 所在行业
    summary = x  # 工作职责
    startDate_school = x  # 入学时间  - 只写年月
    endDate_school = x  # 毕业时间  - 只写年月
    school = x  # 学校名称
    speciality = x  # 就读专业
    academicDegree = x  # 学历
    data = {
    "1822": [{}],
    "1823": [{}],
    "1824": [{}],
    "1825": [{}],
    "applyInfo": {
        "campusSiteId": "null",
        "aimWorkCity": "上海市"
    },
    "uploadInfo": {
        "resumeKey": "",
        "portrait": "null",
        "attachments": []
    },
    "basicInfo": {
        "23329": website,
        "name": name,
        "gender": gender,
        "countryCallingCode": "",
        "phone": phone,
        "fullPhone": phone,
        "email": email,
        "birthDate": birthdate,
        "location": location,
        "academicDegree": academicDegree,
        "graduateDate": {"startDate": graduateDate},
        "startFrom": startFrom
    },
    "jobIntention": {"salary": salary, "aimSalary": aimSalary},
    "experienceInfo": [{
        "startDate": startDate,
        "endDate": endDate,
        "company": company,
        "title": title,
        "location": location_gs,
        "industry": industry,
        "summary": summary
    }],
    "educationInfo": [{
        "startDate": startDate_school,
        "endDate": endDate_school,
        "school": school,
        "speciality": speciality,
        "academicDegree": academicDegree
    }],
    "practiceInfo": [{}],
    "projectInfo": [{}],
    "languageInfo": [{}],
    "selfDescription": {},
    "awardInfo": [{}],
    "device": "pc",
    "recommender": {},
    "recommendInfo": {"recommendReason": ""},
    "siteId": "7524",
    "acquisitionMode": 9
    }
    rr = requests.post(url_tdjl, json=data, headers=h).json()
    print("%s" % rr)
    
    x=x+1
