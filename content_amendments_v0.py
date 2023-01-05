from config.db_tt_ywdata_config_tmp import *
from tqdm import tqdm
import zhconv

def init_rating():
    global increment_time, exp_dir, this_content_table, this_author_table,\
        pp_app_api, cluster_app_api, kw_app_api,\
        this_author_time_name, \
        this_content_time_name, this_content_pp_time_name, this_content_pp_cluster_time_name, this_content_pp_cl_kw_time_name,\
        this_author_content_time_name,\
        bad_cluster_set,\
        pp_threshold,yh_pp_rate_threshold,yh_content_count_threshold,yh_score,seed_pp_rate_threshold,seed_content_count_threshold,seed_score,natual_score,kw_score,\
        yh_cl_score

    increment_time = 0
    # increment_time = time2timeStamp("2022-11-14 00:00:00")
    # increment_time = time2timeStamp(str(zero_yesterday()))
    exp_dir = './tmp_data/'
    this_author_time_name = "tt_author_dict1226_" + str(increment_time) + ".pkl"
    this_content_time_name = "tt_content_dict1226_" + str(increment_time) + ".pkl"

    this_content_pp_time_name = "tt_content_pp_dict1226_" + str(increment_time) + ".pkl"
    this_content_pp_cluster_time_name = "tt_content_pp_cluster_dict1226_" + str(increment_time) + ".pkl"
    this_content_pp_cl_kw_time_name = "tt_content_pp_cl_kw_dict1226_" + str(increment_time) + ".pkl"

    this_author_content_time_name = "tt_author_content_dict1226_" + str(increment_time) + ".pkl"
    this_content_table = tt_ywdata_content1220
    this_author_table = tt_ywdata_author_analysed1220


    nlp_api_ip = "10.96.130.66"

    # pp_app_api = "http://192.168.0.178:8199/predict"
    # cluster_app_api = "http://192.168.0.178:9099/predict"
    # kw_app_api = "http://192.168.0.178:9098/predict"

    pp_app_api = "http://"+nlp_api_ip+":7199/predict"
    cluster_app_api = "http://"+nlp_api_ip+":7099/predict"
    kw_app_api = "http://"+nlp_api_ip+":9098/predict"

    bad_cluster_set = [38, 45, 16, 28]

    pp_threshold = 0.97  # 立场分析确定yh的阈值

    yh_pp_rate_threshold = 0.3
    yh_content_count_threshold = 3
    yh_score = 7

    yh_cl_score = 8

    seed_pp_rate_threshold = 0.5
    seed_content_count_threshold = 5
    seed_score = 10

    kw_score = 9

    natual_score = 0



def content_amend():
    init_rating()
    kw_amend_list = []
    kw_amend_list.append("中华民国")
    kw_amend_list.append("小熊维尼")
    kw_amend_list.append("包子&毛")
    kw_amend_list.append("中国&秘密")
    kw_amend_list.append("屠杀&四")
    kw_amend_list.append("习近平&江泽民")
    kw_amend_list.append("中国&消灭")
    kw_amend_list.append("包子&毒")
    kw_amend_list.append("中国&地狱")
    kw_amend_list.append("包子&杀")
    kw_amend_list.append("习天天")

    with get_tt_ywdata_session() as s:
        # s.query(this_content_table).filter(this_content_table.kw_result in kw_amend_list).update(
        #     {"kw_flag": 0})
        # s.query(this_content_table).filter(this_content_table.kw_result == "中华民国").update(
        #     {"kw_flag": 0})
        s.query(this_content_table).filter(this_content_table.kw_result.in_(kw_amend_list)).update(
            {"kw_flag": 0}, synchronize_session=False)

def account_analysis():
    init_rating()

    # 验证7分用户
    seven_account_dict = {}
    with get_tt_ywdata_session() as s:
        res = s.query(this_author_table).filter(this_author_table.score == 10).all()
        for r in res:
            seven_account_dict[r.author] = [r.tt_number, r.tt_zh_number, r.cluster_bad_number, r.bert_bad_number, r.keyword_bad_number]

    print("账号id", "内容数", "中文内容数", "聚类bad数", "bert bad 数", "关键词bad数")
    for idx, (acc, accv) in enumerate(seven_account_dict.items()):
        print(idx, acc, accv)
        with get_tt_ywdata_session() as s:
            res = s.query(this_content_table).filter(this_content_table.author == acc).all()
            for r in res:
                if len(r.clean_txt.strip()) == 0:
                    continue
                print(idx, [r.clean_txt], r.bert_score,  r.cluster, r.kw_result, r.kw_flag)

        print("##################### -- "+str(idx)+" -- ##########################")



    # with get_tt_ywdata_session() as s:
    #     # s.query(this_content_table).filter(this_content_table.kw_result in kw_amend_list).update(
    #     #     {"kw_flag": 0})
    #     # s.query(this_content_table).filter(this_content_table.kw_result == "中华民国").update(
    #     #     {"kw_flag": 0})
    #     s.query(this_content_table).filter(this_content_table.kw_result.in_(kw_amend_list)).update(
    #         {"kw_flag": 0}, synchronize_session=False)

def account_analysis_output():
    init_rating()

    # 验证7分用户
    seven_account_dict = {}
    with get_tt_ywdata_session() as s:
        res = s.query(this_author_table).filter(this_author_table.score == 9).all()
        for r in res:
            seven_account_dict[r.author] = [r.tt_number, r.tt_zh_number, r.cluster_bad_number, r.bert_bad_number, r.keyword_bad_number]

    with open("./output/score10_res.txt", "a+") as f:
        # print("账号id", "内容数", "中文内容数", "聚类bad数", "bert bad 数", "关键词bad数")
        f.write("账号i ---- 内容数 ---- 中文内容数 ---- 聚类bad数 ---- bert bad 数 ---- 关键词bad数\n")
        for idx, (acc, accv) in enumerate(seven_account_dict.items()):
            # print(idx, acc, accv)
            f.write(str(idx)+str(acc)+str(accv)+"\n")
            f.write("##################### -- " + str(idx) + " -- ##########################\n")
            with get_tt_ywdata_session() as s:
                res = s.query(this_content_table).filter(this_content_table.author == acc).all()
                for r in res:
                    if len(r.clean_txt.strip()) == 0:
                        continue
                    # print(idx, [r.clean_txt], r.bert_score,  r.cluster, r.kw_result, r.kw_flag)
                    f.write(str(idx) + str([r.clean_txt]) +str(r.bert_score) + str(r.cluster)+ str(r.kw_result) +str(r.kw_flag) + "\n")

            # print("##################### -- "+str(idx)+" -- ##########################")


if __name__ == '__main__':
    # content_amend()

    # account_analysis()
    account_analysis_output()
    pass