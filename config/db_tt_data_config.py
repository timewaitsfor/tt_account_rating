from config.db_config import *
import contextlib

# mg tt_data 数据库读取
tt_data_engine = create_engine('mysql+pymysql://root:ZAQ12wssd@10.96.130.69:3306/tt_data?charset=utf8', echo=False)
# mg_engine = create_engine('mysql+pymysql://root:1122@localhost:3306/tt_data?charset=utf8', echo=False)
TT_Data_Session = sessionmaker(bind=tt_data_engine)
TT_Data_Base = declarative_base(tt_data_engine)

@contextlib.contextmanager
def get_tt_data_session():
    s = TT_Data_Session()
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        if "Duplicate entry"  not in str(e):
            print(e)
    finally:
        s.close()

class tt_mg_data_video(TT_Data_Base, BaseMixin):
    __tablename__ = "tt_yh_data_video"
    keyword = Column(String(255), nullable=False)
    labels = Column(String(255), nullable=False)
    nickname = Column(String(255), nullable=False)
    unique_id = Column(String(255), nullable=False)
    avatar_larger = Column(String(255), nullable=False)
    signature = Column(String(255), nullable=False)
    video_desc = Column(String(255), nullable=False) # 之前叫desc
    stats_diggCount = Column(Integer, nullable=False)
    stats_playCount = Column(Integer, nullable=False)
    stats_commentCount = Column(Integer, nullable=False)
    in_time = Column(Integer, nullable=False)
    yh_account_type = Column(String(255), nullable=False)
    is_yh_account = Column(Integer, nullable=False)
    is_hit_key = Column(Integer, nullable=False)
    emo_polarity = Column(String(255), nullable=False)
    directionality = Column(String(255), nullable=False)
    info = Column(String(255), nullable=False)
    is_stop_word = Column(String(255), nullable=False)
    created_time = Column(Integer, nullable=False)
    # video = Column(String(255), nullable=False)
    video_src_url = Column(String(255), nullable=False)
    author_avatar_url = Column(String(255), nullable=False)
    music_id = Column(String(255), nullable=False)
    music_playUrl = Column(String(255), nullable=False)
    music_title = Column(String(255), nullable=False)
    music_authorName = Column(String(255), nullable=False)
    duet_info_duetFromId = Column(String(255), nullable=False)
    for_friend = Column(Integer, nullable=False, unique=True)
    author_followingCount = Column(Integer, nullable=False)
    author_followerCount = Column(Integer, nullable=False)
    author_heartCount = Column(Integer, nullable=False)
    author_videoCount = Column(Integer, nullable=False)
    author_diggCount = Column(Integer, nullable=False)
    private_item = Column(Integer, nullable=False)
    duet_enabled = Column(Integer, nullable=False)
    stitch_enabled = Column(Integer, nullable=False)
    share_enabled = Column(Integer, nullable=False)
    stickers_onItem_stickerText = Column(String(255), nullable=False)
    is_ad = Column(Integer, nullable=False)
    video_status = Column(Integer, nullable=False)
    author_id = Column(Integer, nullable=False)
    video_id = Column(Integer, nullable=False)

class test_tt_yh_data_video(TT_Data_Base, BaseMixin):
    # __tablename__ = "921_tt_yh_data_video"
    __tablename__ = "test_tt_yh_data_video"
    keyword = Column(String(255), nullable=False)
    labels = Column(String(255), nullable=False)
    nickname = Column(String(255), nullable=False)
    unique_id = Column(String(255), nullable=False)
    avatar_larger = Column(String(255), nullable=False)
    signature = Column(String(255), nullable=False)
    video_desc = Column(String(255), nullable=False) # 之前叫desc
    stats_diggCount = Column(Integer, nullable=False)
    stats_playCount = Column(Integer, nullable=False)
    stats_commentCount = Column(Integer, nullable=False)
    in_time = Column(Integer, nullable=False)
    yh_account_type = Column(String(255), nullable=False)
    is_yh_account = Column(Integer, nullable=False)
    is_hit_key = Column(Integer, nullable=False)
    emo_polarity = Column(String(255), nullable=False)
    directionality = Column(String(255), nullable=False)
    info = Column(String(255), nullable=False)
    is_stop_word = Column(String(255), nullable=False)
    created_time = Column(Integer, nullable=False)
    # video = Column(String(255), nullable=False)
    video_src_url = Column(String(255), nullable=False)
    author_avatar_url = Column(String(255), nullable=False)
    music_id = Column(String(255), nullable=False)
    music_playUrl = Column(String(255), nullable=False)
    music_title = Column(String(255), nullable=False)
    music_authorName = Column(String(255), nullable=False)
    duet_info_duetFromId = Column(String(255), nullable=False)
    for_friend = Column(Integer, nullable=False, unique=True)
    author_followingCount = Column(Integer, nullable=False)
    author_followerCount = Column(Integer, nullable=False)
    author_heartCount = Column(Integer, nullable=False)
    author_videoCount = Column(Integer, nullable=False)
    author_diggCount = Column(Integer, nullable=False)
    private_item = Column(Integer, nullable=False)
    duet_enabled = Column(Integer, nullable=False)
    stitch_enabled = Column(Integer, nullable=False)
    share_enabled = Column(Integer, nullable=False)
    stickers_onItem_stickerText = Column(String(255), nullable=False)
    is_ad = Column(Integer, nullable=False)
    video_status = Column(Integer, nullable=False)
    author_id = Column(Integer, nullable=False)
    video_id = Column(Integer, nullable=False)

class tt_pp_mg_posts(TT_Data_Base, BaseMixin):
    __tablename__ = "tt_pp_mg_posts"
    desc = Column(String(1000), nullable=False)
    user_id = Column(String(255), nullable=False)
    # pp_score = Column(FLOAT(precision=11, scale=5))
    pp_score = Column(Float)
    keywords = Column(String(255), nullable=False)

class tt_pp_mg_comments(TT_Data_Base, BaseMixin):
    __tablename__ = "tt_pp_mg_comments"
    txt = Column(String(1000), nullable=False)
    comment_user_id = Column(String(255), nullable=False)
    # pp_score = Column(FLOAT(precision=11, scale=5))
    pp_score = Column(Float)
    keywords = Column(String(255), nullable=False)


class tt_pp_mg_users(TT_Data_Base, BaseMixin):
    __tablename__ = "tt_pp_mg_users"
    mg_post_count = Column(Integer)
    mg_comment_count = Column(Integer)

class tt_ext_comments(TT_Data_Base, BaseMixin):
    __tablename__ = "tt_ext_comments"
    # id = Column(Integer, nullable=False)
    text = Column(String(1000))
    aweme_id = Column(String(255))
    created_time = Column(Integer)
    digg_count = Column(Integer)
    status = Column(Integer)
    user_id = Column(Integer)
    user_unique_id = Column(String(255))
    user_nickname = Column(String(255))
    user_sec_uid = Column(String(255))
    user_avatar_url = Column(String(255))
    reply_comment_cid = Column(String(255))
    reply_comment_text = Column(String(255))
    reply_comment_aweme_id = Column(String(255))
    reply_comment_created_time = Column(Integer)
    reply_comment_digg_count = Column(Integer)
    reply_comment_user_uid = Column(Integer)

    reply_comment_user_nickname = Column(String(255))
    reply_comment_user_sec_uid = Column(String(255))

    reply_comment_reply_id = Column(Integer)
    reply_comment_reply_comment = Column(String(255))

    reply_id = Column(Integer)
    reply_to_reply_id = Column(Integer)
    text_extra_start = Column(Integer)
    text_extra_end = Column(Integer)
    text_euser_id = Column(Integer)

    text_hashtag_name = Column(String(255))
    text_sec_uid = Column(String(255))

    reply_comment_total = Column(Integer)
    is_author_digged = Column(Integer)
    author_pin = Column(Integer)

    # created_at = Column(Integer)
    # updated_at = Column(Integer)


class tt_refine_comments(TT_Data_Base, BaseMixin):
    __tablename__ = "tt_refine_comments"
    text = Column(String(1000), nullable=False)
    aweme_id = Column(String(255))
    digg_count = Column(Integer)
    status = Column(Integer)
    user_id = Column(Integer)
    user_unique_id = Column(String(255))
    user_nickname = Column(String(255))
    user_sec_uid = Column(String(255))
    user_avatar_url = Column(String(255))
    reply_comment_cid = Column(String(255))
    reply_comment_text = Column(String(255))
    reply_comment_aweme_id = Column(String(255))
    reply_comment_created_time = Column(Integer)
    reply_comment_digg_count = Column(Integer)
    reply_comment_user_uid = Column(Integer)

    reply_comment_user_nickname = Column(String(255))
    reply_comment_user_sec_uid = Column(String(255))

    reply_comment_reply_id = Column(Integer)
    reply_comment_reply_comment = Column(String(255))

    reply_id = Column(Integer)
    reply_to_reply_id = Column(Integer)
    text_extra_start = Column(Integer)
    text_extra_end = Column(Integer)
    text_euser_id = Column(Integer)

    text_hashtag_name = Column(String(255))
    text_sec_uid = Column(String(255))

    reply_comment_total = Column(Integer)
    is_author_digged = Column(Integer)
    author_pin = Column(Integer)
    created_time = Column(Integer)

class tt_ext_posts(TT_Data_Base, BaseMixin):
    __tablename__ = "tt_ext_posts"

    video_desc = Column(String(1000), nullable=False)
    created_time = Column(Integer)
    video_src_url = Column(String(255))

    author_id = Column(Integer)
    author_unique_id = Column(String(255))
    author_avatar_url = Column(String(255))
    music_id = Column(String(255))
    music_playUrl = Column(String(255))
    music_title = Column(String(2000))
    music_authorName = Column(String(2000))

    stats_diggCount = Column(Integer)
    stats_shareCount = Column(Integer)
    stats_commentCount = Column(Integer)
    stats_playCount = Column(Integer)

    duet_info_duetFromId = Column(String(255))
    for_friend = Column(Integer)
    author_followingCount = Column(Integer)
    author_followerCount = Column(Integer)
    author_heartCount = Column(Integer)
    author_videoCount = Column(Integer)
    author_diggCount = Column(Integer)
    private_item = Column(Integer)
    duet_enabled = Column(Integer)
    stitch_enabled = Column(Integer)
    share_enabled = Column(Integer)

    stickers_onItem_stickerText = Column(String(255))
    is_ad = Column(Integer)
    video_status = Column(Integer)
    image_state = Column(Integer)

    ocr_result = Column(String(255))
    face_result = Column(String(255))



class tt_refine_posts(TT_Data_Base, BaseMixin):
    __tablename__ = "tt_refine_posts"

    video_desc = Column(String(1000), nullable=False)
    created_time = Column(Integer)
    video_src_url = Column(String(255))
    author_id = Column(BIGINT)
    author_unique_id = Column(String(255))
    author_avatar_url = Column(String(255))
    music_id = Column(String(255))
    music_playUrl = Column(String(255))
    music_title = Column(String(2000))
    music_authorName = Column(String(2000))

    stats_diggCount = Column(Integer)
    stats_shareCount = Column(Integer)
    stats_commentCount = Column(Integer)
    stats_playCount = Column(Integer)

    duet_info_duetFromId = Column(String(255))
    for_friend = Column(Integer)
    author_followingCount = Column(Integer)
    author_followerCount = Column(Integer)
    author_heartCount = Column(Integer)
    author_videoCount = Column(Integer)
    author_diggCount = Column(Integer)
    private_item = Column(Integer)
    duet_enabled = Column(Integer)
    stitch_enabled = Column(Integer)
    share_enabled = Column(Integer)

    stickers_onItem_stickerText = Column(String(255))
    is_ad = Column(Integer)
    video_status = Column(Integer)
    image_state = Column(Integer)

    ocr_result = Column(String(255))
    face_result = Column(String(255))

if __name__ == "__main__":
    # 创建表的原子操作
    # Base.metadata.create_all(engine)

    pass