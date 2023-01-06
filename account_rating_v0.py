# from config.db_tt_ywdata_config import *
from config.db_tt_ywdata_config import *
from utils.mo_utils import *
from utils.preprocess_text import *
from tqdm import tqdm

from sqlalchemy  import func

import random
from datetime import datetime

import requests
import ast

from flashtext import KeywordProcessor

def exp_cluster_rating():

    increment_time = 0
    # cluster_label = load_pickle("./cluster_api/cluster_model/cluster_label.pkl")
    #
    # bad_cluster_level = 3
    # bad_cluster_set = set()
    # for ck, cv in cluster_label.items():
    #     this_cluster_lvl = int(cv['label'])
    #     if this_cluster_lvl >= bad_cluster_level:
    #         bad_cluster_set.add(ck)
    #
    # print(bad_cluster_set)
    # bad_cluster_set.remove(10)

    # bad_cluster_set = [10] # 1
    # bad_cluster_set = [7] # 1
    # bad_cluster_set = [38] # 少量
    # bad_cluster_set = [39] # 只有台湾
    # bad_cluster_set = [42] # 1~2
    # bad_cluster_set = [45] # 多
    # bad_cluster_set = [14] # 模棱两可
    # bad_cluster_set = [14] # 模棱两可
    # bad_cluster_set = [47] # 类少且无
    # bad_cluster_set = [16] # 少量
    # bad_cluster_set = [49] # 无
    # bad_cluster_set = [28] # 少量

    bad_cluster_set = [38, 45, 16, 28]





    # this_author_content_time_name = "tt_author_content_dict_" + str(increment_time) + ".pkl"
    # this_content_time_name = "tt_content_cluster_dict_" + str(increment_time) + ".pkl"
    # this_author_time_name = "tt_author_dict_" + str(increment_time) + ".pkl"


    tt_author_content_dict = load_pickle(exp_dir + this_author_content_time_name)
    tt_content_dict = load_pickle(exp_dir + this_content_pp_cluster_time_name)
    tt_author_dict = load_pickle(exp_dir + this_author_time_name)



    seed_author_dict = {}
    yh_author_dict = {}
    # for i, (aid, av) in enumerate(tqdm(tt_author_content_dict.items())):
    for i, (aid, av) in enumerate(tt_author_content_dict.items()):

        # [author, author_id, tt_text, tt_type, clean_txt, publish_date, save_time, video_id, video_src_url,
        #  music_playUrl, music_title, stats_diggCount, stats_shareCount, stats_commentCount, stats_playCount,
        #  created_at, updated_at, ocr_result, face_result, ocr_flag, face_flag, task_id, bert_score, cluster]

        sample_content = av[list(av.keys())[0]]
        author = sample_content[0]
        author_id = sample_content[1]
        tt_number = len(tt_author_dict[aid])
        tt_zh_number = len(av)
        # bert_bad_number = sample_content[0]
        save_time = current_timestamp()

        cluster_bad_number = 0
        for j, (cid, cv) in enumerate(av.items()):
            this_txt = tt_content_dict[cid][4]

            # if "习" not in this_txt:
            #     continue

            this_cluster = tt_content_dict[cid][-1]
            bert_score = tt_content_dict[cid][-2]



            # if bert_score > 0.9:
            #     print("bert find", cv[4], tt_content_dict[cid][-1], tt_content_dict[cid][-2])

            # if this_cluster in bad_cluster_set and bert_score>0.9:
            if this_cluster in bad_cluster_set:
                cluster_bad_number += 1
            #     print("bert find", cv[4], tt_content_dict[cid][-1], tt_content_dict[cid][-2])


        # cluster_bad_rate = float(cluster_bad_number)/tt_zh_number
        # if cluster_bad_number >= 1 and cluster_bad_rate>=0.8:
        # if cluster_bad_number >= 1:
        #     print()
        #     for avk, avv in av.items():
        #         if tt_content_dict[avk][-2] > 0.9 and tt_content_dict[avk][-1] in bad_cluster_set:
        #             print(avk, avv[4], tt_content_dict[avk][-1], tt_content_dict[avk][-2])

        if cluster_bad_number >= 5:
            print()
            print(author_id)
            for avk, avv in av.items():
                # if tt_content_dict[avk][-2] > 0.9 and tt_content_dict[avk][-1] in bad_cluster_set:
                # if tt_content_dict[avk][-2] > 0.9 and tt_content_dict[avk][-1] in bad_cluster_set:
                # if "习" not in tt_content_dict[avk][4] or tt_content_dict[avk][-1] not in bad_cluster_set:
                #     continue
                if tt_content_dict[avk][-1] in bad_cluster_set:
                    print(avk, avv[4], tt_content_dict[avk][-1], tt_content_dict[avk][-2])


        # bert_bad_number = 0
        # for j, (cid, cv) in enumerate(av.items()):
        #     this_pp_score =
        #     cv[-2]
        #     if this_pp_score > pp_threshold:
        #         bert_bad_number += 1
        # this_pp_rate = bert_bad_number / tt_zh_number
        # if this_pp_rate >= seed_pp_rate_threshold and tt_zh_number >= seed_content_count_threshold:
        #     with get_tt_ywdata_session() as s:
        #         s.add(this_author_table(author=author, author_id=author_id, tt_number=tt_number,
        #                                         tt_zh_number=tt_zh_number, bert_bad_number=bert_bad_number,
        #                                         save_time=save_time, score=seed_score))
        #         s.query(this_author_table).filter(this_author_table.author_id == author_id).update(
        #             {"score": seed_score})
        #     seed_author_dict[author_id] = [author, author_id, tt_number, tt_zh_number, bert_bad_number, save_time,
        #                                    seed_score]
        #
        # elif this_pp_rate >= yh_pp_rate_threshold and tt_zh_number >= yh_content_count_threshold:
        #     with get_tt_ywdata_session() as s:
        #         s.add(this_author_table(author=author, author_id=author_id, tt_number=tt_number,
        #                                         tt_zh_number=tt_zh_number, bert_bad_number=bert_bad_number,
        #                                         save_time=save_time, score=yh_score))
        #         s.query(this_author_table).filter(this_author_table.author_id == author_id).update(
        #             {"score": yh_score})
        #     yh_author_dict[author_id] = [author, author_id, tt_number, tt_zh_number, bert_bad_number, save_time,
        #                                  yh_score]
        # else:
        #     with get_tt_ywdata_session() as s:
        #         s.add(this_author_table(author=author, author_id=author_id, tt_number=tt_number,
        #                                         tt_zh_number=tt_zh_number, bert_bad_number=bert_bad_number,
        #                                         save_time=save_time, score=natual_score))
        #     pass

def exp_read_tt_author_contents_increment(increment_time, off_mod=True):

    if off_mod == True:
        tt_author_dict = load_pickle(exp_dir + this_author_time_name)
        tt_content_dict = load_pickle(exp_dir + this_content_time_name)
    else:
        tt_author_dict = {}
        tt_content_dict = {}
        active_post_count =  0
        with get_tt_ywdata_session() as s:
            # res = s.query(this_content_table).filter(this_content_table.created_at > increment_time).all()
            res = s.query(this_content_table).all()
            for r in tqdm(res):
                this_id = r.id
                author_id = r.author_id
                if author_id not in tt_author_dict:
                    tt_author_dict[author_id] = []
                tt_author_dict[author_id].append(this_id)

                clean_txt = r.clean_txt

                # this_text_raw = r.tt_text
                # this_text = filter_illegal_char(this_text_raw)
                # filtered_content = preprocess_text(this_text, max_sentence_length=255, min_sentence_length=6)
                #
                # # if len(filtered_content) > 1:
                # #     continue
                #
                # if len(filtered_content) != 1:
                #     # print("filter error:", this_id, filtered_content)
                #     continue
                #
                # if len(filtered_content[0]) < 6 or len(filtered_content[0]) >= 255:
                #     # print("filter so short error:", len(filtered_content[0]), this_id, filtered_content)
                #     continue

                active_post_count += 1
                author = r.author
                tt_text = r.tt_text
                tt_type = r.tt_type
                # clean_txt = filtered_content # 由过滤得到的文本
                clean_txt = clean_txt # 由过滤得到的文本
                publish_date = r.publish_date
                save_time = r.save_time
                video_id = r.video_id
                video_author = r.video_author
                video_author_id = r.video_author_id
                video_src_url = r.video_src_url
                music_playUrl = r.music_playUrl
                music_title = r.music_title
                stats_diggCount = r.stats_diggCount
                stats_shareCount = r.stats_shareCount
                stats_commentCount = r.stats_commentCount
                stats_playCount = r.stats_playCount
                created_at = r.created_at
                updated_at = r.updated_at
                ocr_result = r.ocr_result
                face_result = r.face_result
                ocr_flag = r.ocr_flag
                face_flag = r.face_flag
                task_id = r.task_id
                bert_score = r.bert_score
                cluster = r.cluster
                tt_content_dict[this_id] = [author, author_id, tt_text, tt_type, clean_txt, publish_date, save_time,
                                            video_id, video_author, video_author_id, video_src_url, music_playUrl, music_title, stats_diggCount,
                                            stats_shareCount, stats_commentCount, stats_playCount, created_at,
                                            updated_at, ocr_result, face_result, ocr_flag, face_flag, task_id,
                                            bert_score, cluster]
        print("active post count:", active_post_count)
        generate_pickle(exp_dir + this_content_time_name, tt_content_dict)
        generate_pickle(exp_dir+this_author_time_name, tt_author_dict)
    return tt_content_dict, tt_author_dict

def read_tt_author_contents_increment(increment_time, off_mod=True):
    if off_mod == True:
        tt_author_dict = load_pickle(exp_dir + this_author_time_name)
        tt_content_dict = load_pickle(exp_dir + this_content_time_name)
    else:
        tt_author_dict = {}
        tt_content_dict = {}
        active_post_count =  0
        with get_tt_ywdata_session() as s:
            # res = s.query(tt_ywdata_content).filter(tt_ywdata_content.created_at > increment_time).all()
            res = s.query(this_content_table).all()
            for r in tqdm(res):
                this_id = r.id
                author_id = r.author_id
                if author_id not in tt_author_dict:
                    tt_author_dict[author_id] = []
                tt_author_dict[author_id].append(this_id)

                this_text_raw = r.tt_text
                this_text = filter_illegal_char(this_text_raw)
                filtered_content = preprocess_text(this_text, max_sentence_length=255, min_sentence_length=6)

                # if len(filtered_content) > 1:
                #     continue

                if len(filtered_content) != 1:
                    # print("filter error:", this_id, filtered_content)
                    continue

                if len(filtered_content[0]) < 6 or len(filtered_content[0]) >= 255:
                    # print("filter so short error:", len(filtered_content[0]), this_id, filtered_content)
                    continue

                active_post_count += 1
                author = r.author
                tt_text = r.tt_text
                tt_type = r.tt_type
                clean_txt = filtered_content # 由过滤得到的文本
                publish_date = r.publish_date
                save_time = r.save_time
                video_id = r.video_id
                video_author = r.video_author
                video_author_id = r.video_author_id
                video_src_url = r.video_src_url
                music_playUrl = r.music_playUrl
                music_title = r.music_title
                stats_diggCount = r.stats_diggCount
                stats_shareCount = r.stats_shareCount
                stats_commentCount = r.stats_commentCount
                stats_playCount = r.stats_playCount
                created_at = r.created_at
                updated_at = r.updated_at
                ocr_result = r.ocr_result
                face_result = r.face_result
                ocr_flag = r.ocr_flag
                face_flag = r.face_flag
                task_id = r.task_id
                bert_score = r.bert_score
                cluster = r.cluster
                tt_content_dict[this_id] = [author, author_id, tt_text, tt_type, clean_txt, publish_date, save_time,
                                            video_id, video_author, video_author_id, video_src_url, music_playUrl, music_title, stats_diggCount,
                                            stats_shareCount, stats_commentCount, stats_playCount, created_at,
                                            updated_at, ocr_result, face_result, ocr_flag, face_flag, task_id,
                                            bert_score, cluster]
        print("active post count:", active_post_count)
        generate_pickle(exp_dir + this_content_time_name, tt_content_dict)
        generate_pickle(exp_dir+this_author_time_name, tt_author_dict)
    return tt_content_dict, tt_author_dict

def read_tt_author_post_contents_increment(increment_time, off_mod=True):
    if off_mod == True:
        tt_author_dict = load_pickle(exp_dir + this_author_time_name)
        tt_content_dict = load_pickle(exp_dir + this_content_time_name)
    else:
        tt_author_dict = {}
        tt_content_dict = {}
        active_post_count =  0


        iterate_token = True
        update_list = []
        while True:
            with get_tt_ywdata_session() as s:
                # res = s.query(tt_ywdata_content).filter(tt_ywdata_content.created_at > increment_time).all()

                # increment_time = 0
                # increment_time = time2timeStamp("2022-12-01 00:00:00")
                # increment_time = time2timeStamp("2022-12-20 00:00:00") # 1671465600

                # res = s.query(this_content_table).filter(this_content_table.tt_type == 0)
                # res = s.query(this_content_table).filter(this_content_table.tt_type == 0 and this_content_table.created_at < increment_time).all()
                # res = s.query(this_content_table).filter(this_content_table.tt_type == 0  and this_content_table.created_at < increment_time and this_content_table.ana_flag == 0).limit(10000).all()
                res = s.query(this_content_table).filter(this_content_table.tt_type == 0, this_content_table.ana_flag == 0).limit(10000).all()

                if len(res) == 0:
                    # iterate_token = False
                    break

                for r in tqdm(res):
                    this_id = r.id
                    author_id = r.author_id

                    update_list.append(this_id)
                    if author_id not in tt_author_dict:
                        tt_author_dict[author_id] = []
                    tt_author_dict[author_id].append(this_id)

                    this_text_raw = r.tt_text
                    this_text = filter_illegal_char(this_text_raw)
                    filtered_content = preprocess_text(this_text, max_sentence_length=255, min_sentence_length=6)

                    # if len(filtered_content) > 1:
                    #     continue

                    if len(filtered_content) != 1:
                        # print("filter error:", this_id, filtered_content)
                        continue

                    if len(filtered_content[0]) < 6 or len(filtered_content[0]) >= 255:
                        # print("filter so short error:", len(filtered_content[0]), this_id, filtered_content)
                        continue

                    active_post_count += 1
                    author = r.author
                    tt_text = r.tt_text
                    tt_type = r.tt_type
                    clean_txt = filtered_content # 由过滤得到的文本
                    publish_date = r.publish_date
                    save_time = r.save_time
                    video_id = r.video_id
                    video_author = r.video_author
                    video_author_id = r.video_author_id
                    video_src_url = r.video_src_url
                    music_playUrl = r.music_playUrl
                    music_title = r.music_title
                    stats_diggCount = r.stats_diggCount
                    stats_shareCount = r.stats_shareCount
                    stats_commentCount = r.stats_commentCount
                    stats_playCount = r.stats_playCount
                    created_at = r.created_at
                    updated_at = r.updated_at
                    ocr_result = r.ocr_result
                    face_result = r.face_result
                    ocr_flag = r.ocr_flag
                    face_flag = r.face_flag
                    task_id = r.task_id
                    bert_score = r.bert_score
                    cluster = r.cluster
                    kw_result = r.kw_result
                    kw_flag = r.kw_flag
                    ana_flag = r.ana_flag
                    tt_content_dict[this_id] = [author, author_id, tt_text, tt_type, clean_txt, publish_date, save_time,
                                                video_id, video_author, video_author_id, video_src_url, music_playUrl, music_title, stats_diggCount,
                                                stats_shareCount, stats_commentCount, stats_playCount, created_at,
                                                updated_at, ocr_result, face_result, ocr_flag, face_flag, task_id,
                                                bert_score, cluster,kw_result,kw_flag]

            with get_tt_ywdata_session() as s:
                s.query(this_content_table).filter(this_content_table.id.in_(update_list)).update(
                    {"ana_flag": 1})
            update_list = []

        print("active post count:", active_post_count)
        generate_pickle(exp_dir + this_content_time_name, tt_content_dict)
        generate_pickle(exp_dir+this_author_time_name, tt_author_dict)
    return tt_content_dict, tt_author_dict

def pre_label_pp_scores(increment_time, off_mod=True):
    start_time = datetime.now()
    print("开始时间：", start_time)
    if off_mod == True:
        tt_content_dict = load_pickle(exp_dir + this_content_pp_time_name)
    else:
        tt_content_dict = load_pickle(exp_dir + this_content_time_name)
        request_count = 0

        posts = []
        post_ids = []
        for i, (cid, cv) in enumerate(tqdm(tt_content_dict.items())):
            # for post_id, post_v in this_acc_posts.items():
            post_text = cv[4][0]
            posts.append(post_text[:120])
            post_ids.append(cid)
            if len(posts) == 200:
                inputstr = {"str": posts}
                ret = requests.post(pp_app_api, json=inputstr)
                this_pp_res = ast.literal_eval(ret.text)
                this_pp_score = this_pp_res['logits']
                for pi, pid in enumerate(post_ids):
                    request_count += 1
                    tt_content_dict[pid][-4] = this_pp_score[pi][0]
                posts = []
                post_ids = []

            if i%10000==0:
                this_time = datetime.now()
                print(this_time, "完成获取pp分数", i)

        if len(posts) != 0:
            inputstr = {"str": posts}
            # time.sleep(1)
            ret = requests.post(pp_app_api, json=inputstr)
            this_pp_res = ast.literal_eval(ret.text)
            this_pp_score = this_pp_res['logits']
            for pi, pid in enumerate(post_ids):
                request_count += 1
                tt_content_dict[pid][-4] = this_pp_score[pi][0]
                # print(pi, request_count, tt_content_dict[pid][1], "posts", posts[pi], this_pp_score[pi][0])

        # this_content_time_name = "tt_content_pp_dict_" + str(increment_time) + ".pkl"
        generate_pickle(exp_dir + this_content_pp_time_name, tt_content_dict)

    end_time = datetime.now()
    print("结束时间：", end_time)
    print("执行时间：", end_time-start_time)
    return  tt_content_dict

def pre_label_cluster_scores(increment_time, off_mod=True):
    start_time = datetime.now()
    print("cluster开始时间：", start_time)
    if off_mod == True:
        tt_content_dict = load_pickle(exp_dir + this_content_pp_cluster_time_name)
    else:
        tt_content_dict = load_pickle(exp_dir + this_content_pp_time_name)
        request_count = 0

        posts = []
        post_ids = []
        for i, (cid, cv) in enumerate(tqdm(tt_content_dict.items())):
            # for post_id, post_v in this_acc_posts.items():
            post_text = cv[4][0]
            posts.append(post_text[:120])
            post_ids.append(cid)
            if len(posts) == 200:
                inputstr = {"str": posts}
                # time.sleep(1)
                ret = requests.post(cluster_app_api, json=inputstr)
                this_cluster_res = ast.literal_eval(ret.text)
                this_cluster_score = this_cluster_res['logits']
                for pi, pid in enumerate(post_ids):
                    request_count += 1
                    tt_content_dict[pid][-3] = this_cluster_score[pi]
                    # print(i, request_count, tt_content_dict[pid][1], "posts", posts[pi], this_cluster_score[pi][0])
                posts = []
                post_ids = []

            if i%10000==0:
                this_time = datetime.now()
                print(this_time, "完成获取cluster分数", i)

        if len(posts) != 0:
            inputstr = {"str": posts}
            # time.sleep(1)
            ret = requests.post(cluster_app_api, json=inputstr)
            this_cluster_res = ast.literal_eval(ret.text)
            this_cluster_score = this_cluster_res['logits']
            for pi, pid in enumerate(post_ids):
                request_count += 1
                tt_content_dict[pid][-3] = this_cluster_score[pi]
                # print(pi, request_count, tt_content_dict[pid][1], "posts", posts[pi], this_cluster_score[pi][0])

        # this_content_time_name = "tt_content_cluster_dict_" + str(increment_time) + ".pkl"
        generate_pickle(exp_dir + this_content_pp_cluster_time_name, tt_content_dict)

    end_time = datetime.now()
    print("cluster结束时间：", end_time)
    print("cluster执行时间：", end_time-start_time)
    return  tt_content_dict

def pre_label_kw_scores(increment_time, off_mod=True):
    start_time = datetime.now()
    print("kw开始时间：", start_time)
    if off_mod == True:
        tt_content_dict = load_pickle(exp_dir + this_content_pp_cl_kw_time_name)
    else:
        tt_content_dict = load_pickle(exp_dir + this_content_pp_cluster_time_name)
        request_count = 0

        posts = []
        post_ids = []
        for i, (cid, cv) in enumerate(tqdm(tt_content_dict.items())):
            # for post_id, post_v in this_acc_posts.items():
            post_text = cv[4][0]
            posts.append(post_text[:120])
            post_ids.append(cid)
            if len(posts) == 200:
                inputstr = {"str": posts}
                # time.sleep(1)
                ret = requests.post(kw_app_api, json=inputstr)
                this_cluster_res = ast.literal_eval(ret.text)
                this_cluster_score = this_cluster_res['logits']
                for pi, pid in enumerate(post_ids):
                    request_count += 1

                    if this_cluster_score[pi] == "#":
                        tt_content_dict[pid][-1] = 0
                    else:
                        tt_content_dict[pid][-1] = 1
                        tt_content_dict[pid][-2] = this_cluster_score[pi]

                    # tt_content_dict[pid][-1] = this_cluster_score[pi]
                    # print(i, request_count, tt_content_dict[pid][1], "posts", posts[pi], this_cluster_score[pi][0])
                posts = []
                post_ids = []

            if i%10000==0:
                this_time = datetime.now()
                print(this_time, "完成获取kw分数", i)

        if len(posts) != 0:
            inputstr = {"str": posts}
            # time.sleep(1)
            ret = requests.post(kw_app_api, json=inputstr)
            this_cluster_res = ast.literal_eval(ret.text)
            this_cluster_score = this_cluster_res['logits']
            for pi, pid in enumerate(post_ids):
                request_count += 1
                # tt_content_dict[pid][-1] = this_cluster_score[pi]

                if this_cluster_score[pi] == "#":
                    tt_content_dict[pid][-1] = 0
                else:
                    tt_content_dict[pid][-1] = 1
                    tt_content_dict[pid][-2] = this_cluster_score[pi]
                # print(pi, request_count, tt_content_dict[pid][1], "posts", posts[pi], this_cluster_score[pi][0])

        # this_content_time_name = "tt_content_cluster_dict_" + str(increment_time) + ".pkl"
        generate_pickle(exp_dir + this_content_pp_cl_kw_time_name, tt_content_dict)

    end_time = datetime.now()
    print("kw结束时间：", end_time)
    print("kw执行时间：", end_time-start_time)
    return  tt_content_dict

'''
可以更新clean_text、pp_score、cluster到content表，也可以return用户的content信息dict
'''
def update_tt_contents_increment(increment_time, off_mod=True):
    start_time = datetime.now()
    print("开始时间：", start_time)
    # this_content_time_name = "tt_content_pp_dict_" + str(increment_time) + ".pkl"
    # this_author_content_time_name = "tt_author_content_dict_" + str(increment_time) + ".pkl"
    if off_mod == True:
        tt_author_content_dict = load_pickle(exp_dir + this_author_content_time_name)
    else:
        tt_content_dict = load_pickle(exp_dir + this_content_pp_cl_kw_time_name)
        tt_author_content_dict = {}
        for i, (cid, cv) in enumerate(tqdm(tt_content_dict.items())):
            # if i < 1047090:
            #     continue

            author_id = cv[1]
            if author_id not in tt_author_content_dict:
                tt_author_content_dict[author_id] = {}

            tt_author_content_dict[author_id][cid] = cv
            clean_text = cv[4]

            kw_hit = cv[-2]
            kw_flag = cv[-1]

            pp_score = float('%.3f' % cv[-4])
            cluster_res = cv[-3]
            with get_tt_ywdata_session() as s:
                # s.query(this_content_table).filter(this_content_table.id==cid).update({"clean_txt": clean_text, "kw_result":kw_hit, "kw_flag":kw_flag, "bert_score": pp_score, "cluster": cluster_res, "ana_flag": 1})
                s.query(this_content_table).filter(this_content_table.id==cid).update({"clean_txt": clean_text, "kw_result":kw_hit, "kw_flag":kw_flag, "bert_score": pp_score, "cluster": cluster_res})

        print("清洗之后的账号总数：", len(tt_author_content_dict))
        generate_pickle(exp_dir + this_author_content_time_name, tt_author_content_dict)

    return tt_author_content_dict


def debug_ck_pp_score():
    # tt_content_dict = load_pickle(exp_dir + this_content_pp_cluster_time_name)
    tt_content_dict = load_pickle(exp_dir + this_content_pp_time_name)
    for i, (cid, cv) in enumerate(tqdm(tt_content_dict.items())):
        # if i < 1047090:
        #     continue

        pp_score_raw = cv[-2]
        pp_score = float('%.3f' % cv[-2])

        # TODO: debug 2022-12-6 17:15:59
        if pp_score > 10:
            print()


def insert_tt_author_analysed_increment(increment_time, off_mod=True):
    start_time = datetime.now()
    print("插入author_analysed表开始时间：", start_time)
    if off_mod == True:
        # tt_content_dict = load_pickle(exp_dir + this_content_time_name)
        # seed_author_dict = load_pickle(exp_dir + this_seed_author_time_name)
        pass
    else:
        # tt_content_dict = load_pickle(exp_dir + this_content_time_name)
        tt_author_dict = load_pickle(exp_dir + this_author_time_name)
        tt_author_content_dict = load_pickle(exp_dir + this_author_content_time_name)
        seed_author_dict = {}
        yh_author_dict = {}

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

        for i, (aid, av) in enumerate(tqdm(tt_author_content_dict.items())):

            # [author, author_id, tt_text, tt_type, clean_txt, publish_date, save_time, video_id, video_src_url,
            #  music_playUrl, music_title, stats_diggCount, stats_shareCount, stats_commentCount, stats_playCount,
            #  created_at, updated_at, ocr_result, face_result, ocr_flag, face_flag, task_id, bert_score, cluster]

            sample_content = av[list(av.keys())[0]]
            author = sample_content[0]
            author_id = sample_content[1]
            tt_number = len(tt_author_dict[aid])
            tt_zh_number = len(av)
            # bert_bad_number = sample_content[0]
            save_time = current_timestamp()

            base_kw_list = get_kw()
            base_keyword_processor = KeywordProcessor()
            base_keyword_processor.add_keywords_from_list(list(base_kw_list))

            bert_bad_number = 0
            for j, (cid, cv) in enumerate(av.items()):
                this_text = cv[4][0]
                base_keywords_found = base_keyword_processor.extract_keywords(this_text)

                this_pp_score = cv[-4]
                if (this_pp_score > pp_threshold01 and base_keywords_found) or this_pp_score > pp_threshold02:
                    bert_bad_number += 1

            cluster_bad_number = 0
            for j, (cid, cv) in enumerate(av.items()):
                this_cluster = cv[-3]
                if this_cluster in bad_cluster_set:
                    cluster_bad_number += 1

            kw_bad_number = 0
            for j, (cid, cv) in enumerate(av.items()):
                this_kw_label = cv[-1]
                this_kw_result = cv[-2]
                if this_kw_label == 1 and this_kw_result not in kw_amend_list:
                    kw_bad_number += 1

            if kw_bad_number >= 1:
                with get_tt_ywdata_session() as s:
                    s.add(this_author_table(author=author, author_id=author_id, tt_number=tt_number, tt_zh_number=tt_zh_number, bert_bad_number=bert_bad_number, keyword_bad_number=kw_bad_number, save_time=save_time, score=kw_score))
                    s.query(this_author_table).filter(this_author_table.author_id == author_id).update(
                        {"score": kw_score})
                seed_author_dict[author_id] = [author, author_id, tt_number, tt_zh_number, bert_bad_number, kw_bad_number, save_time,
                                               kw_score]
                continue

            this_pp_rate = bert_bad_number / tt_zh_number
            if this_pp_rate >= seed_pp_rate_threshold and tt_zh_number >= seed_content_count_threshold:
                with get_tt_ywdata_session() as s:
                    s.add(this_author_table(author=author, author_id=author_id, tt_number=tt_number, tt_zh_number=tt_zh_number, bert_bad_number=bert_bad_number,  keyword_bad_number=kw_bad_number, save_time=save_time, score=seed_score))
                    s.query(this_author_table).filter(this_author_table.author_id == author_id).update(
                        {"score": seed_score})
                seed_author_dict[author_id] = [author, author_id, tt_number, tt_zh_number, bert_bad_number, kw_bad_number, save_time, seed_score]

            elif this_pp_rate >= yh_pp_rate_threshold and tt_zh_number >= yh_content_count_threshold:

                if cluster_bad_number >= 5:
                    with get_tt_ywdata_session() as s:
                        s.add(this_author_table(author=author, author_id=author_id, tt_number=tt_number, tt_zh_number=tt_zh_number, bert_bad_number=bert_bad_number,  keyword_bad_number=kw_bad_number, save_time=save_time, score=yh_score))
                        s.query(this_author_table).filter(this_author_table.author_id == author_id).update(
                            {"score": yh_cl_score})
                    yh_author_dict[author_id] = [author, author_id, tt_number, tt_zh_number, bert_bad_number,kw_bad_number,  save_time,
                                                   yh_cl_score]
                else:
                    with get_tt_ywdata_session() as s:
                        s.add(this_author_table(author=author, author_id=author_id, tt_number=tt_number, tt_zh_number=tt_zh_number, bert_bad_number=bert_bad_number,  keyword_bad_number=kw_bad_number, save_time=save_time, score=yh_score))
                        s.query(this_author_table).filter(this_author_table.author_id == author_id).update(
                            {"score": yh_score})
                    yh_author_dict[author_id] = [author, author_id, tt_number, tt_zh_number, bert_bad_number, kw_bad_number, save_time,
                                                   yh_score]
            else:
                with get_tt_ywdata_session() as s:
                    s.add(this_author_table(author=author, author_id=author_id, tt_number=tt_number, tt_zh_number=tt_zh_number, bert_bad_number=bert_bad_number,  keyword_bad_number=kw_bad_number, save_time=save_time, score=natual_score))
                pass

    # generate_pickle(exp_dir + this_seed_author_time_name, seed_author_dict)
    print("seed_author_dict count", len(seed_author_dict))
    print("yh_author_dict count", len(yh_author_dict))

    end_time = datetime.now()
    print("插入author_analysed表结束时间：", end_time)
    print("插入author_analysed表执行时间：", end_time-start_time)
    return seed_author_dict


def get_kw():
    base_kw_file = "base_kw_file"
    base_kw_f = open("./data/" + base_kw_file, "r")
    base_kw_raw = base_kw_f.readlines()

    base_keywords = []
    for base_kw in base_kw_raw:
        base_kw = base_kw.strip()
        base_kw = zhconv.convert(base_kw, 'zh-cn')
        if len(base_kw) != 0:
            base_keywords.append(base_kw)

    return base_keywords


def init_rating():
    global increment_time, exp_dir, this_content_table, this_author_table,\
        pp_app_api, cluster_app_api, kw_app_api,\
        this_author_time_name, \
        this_content_time_name, this_content_pp_time_name, this_content_pp_cluster_time_name, this_content_pp_cl_kw_time_name,\
        this_author_content_time_name,\
        bad_cluster_set,\
        pp_threshold01,pp_threshold02,\
        yh_pp_rate_threshold,yh_content_count_threshold,yh_score,seed_pp_rate_threshold,seed_content_count_threshold,seed_score,natual_score,kw_score,\
        yh_cl_score

    increment_time = 0
    # increment_time = time2timeStamp("2022-11-14 00:00:00")
    # increment_time = time2timeStamp(str(zero_yesterday()))
    # print(str(zero_yesterday()))

    exp_dir = './cache_data/'
    this_author_time_name = "tt_author_dict_" + str(increment_time) + ".pkl"
    this_content_time_name = "tt_content_dict_" + str(increment_time) + ".pkl"

    this_content_pp_time_name = "tt_content_pp_dict_" + str(increment_time) + ".pkl"
    this_content_pp_cluster_time_name = "tt_content_pp_cluster_dict_" + str(increment_time) + ".pkl"
    this_content_pp_cl_kw_time_name = "tt_content_pp_cl_kw_dict_" + str(increment_time) + ".pkl"

    this_author_content_time_name = "tt_author_content_dict_" + str(increment_time) + ".pkl"
    this_content_table = tt_ywdata_content
    this_author_table = tt_ywdata_author_analysed


    # nlp_api_ip = "10.96.130.66"

    pp_app_api = "http://192.168.0.178:8199/predict"
    cluster_app_api = "http://192.168.0.178:9099/predict"
    kw_app_api = "http://192.168.0.178:9098/predict"

    # pp_app_api = "http://"+nlp_api_ip+":7199/predict"
    # cluster_app_api = "http://"+nlp_api_ip+":7099/predict"
    # kw_app_api = "http://"+nlp_api_ip+":9098/predict"

    bad_cluster_set = [38, 45, 16, 28]

    pp_threshold01 = 0.9  # 立场分析确定yh的阈值
    pp_threshold02 = 0.99  # 立场分析确定yh的阈值

    yh_pp_rate_threshold = 0.3
    yh_content_count_threshold = 3
    yh_score = 7

    yh_cl_score = 8

    seed_pp_rate_threshold = 0.5
    seed_content_count_threshold = 5
    seed_score = 10

    kw_score = 9

    natual_score = 0

def rating_accounts():
    '''

    :return:
    '''

    init_rating()

    off_mode_token = True
    '''
    按时间戳读取数据，主要是content表
    '''
    tt_content_dict, tt_author_dict = read_tt_author_post_contents_increment(increment_time, off_mod=off_mode_token)

    off_mode_token = False
    '''
    获取每条content的立场分数
    '''
    tt_content_pp_dict = pre_label_pp_scores(increment_time, off_mod=off_mode_token)


    '''
    获取每条content的聚类类别分数
    '''
    tt_content_pp_dict = pre_label_cluster_scores(increment_time, off_mod=off_mode_token)

    # off_mode_token = False
    '''
    获取每条content的关键词
    '''
    tt_content_pp_dict = pre_label_kw_scores(increment_time, off_mod=off_mode_token)

    '''
    更新每条content的聚类类别、立场分数，并得到用户附带content信息的dict
    '''

    # off_mode_token = False
    tt_author_content_dict = update_tt_contents_increment(increment_time, off_mod=off_mode_token)


    off_mode_token = False
    # '''
    # 为用户打分，并插入author_analysed表，并得到输送给task的用户dict
    # '''
    seed_author_dict = insert_tt_author_analysed_increment(increment_time, off_mod=off_mode_token)


if __name__ == '__main__':
    rating_accounts()
    pass
