from utils.mo_utils import *
from config.db_config import *

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    DateTime,
    String,
    Float,
)
import datetime
import contextlib
from sqlalchemy.dialects.mysql import FLOAT



# tiktok 数据库读取
engine = create_engine('mysql+pymysql://root:ZAQ12wssd@10.96.130.69:3306/tiktok?charset=utf8', echo=False)
# engine = create_engine('mysql+pymysql://root:1122@localhost:3306/tiktok?charset=utf8', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base(engine)


@contextlib.contextmanager
def get_session():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()

class tt_keywords(Base, BaseMixin):
    __tablename__ = "tt_keywords"
    keyword = Column(String(36), nullable=False, unique=True)
    label_1 = Column(String(36))
    label_2 = Column(String(36))
    label_3 = Column(String(36))
    ent_type = Column(Integer, nullable=False)
    source = Column(FLOAT(precision=11, scale=2))
    emo_polarity = Column(Integer)
    is_stop_word = Column(Integer) #是否是停用词
    confidence = Column(String(36), default="1")
    info = Column(String(255))
    directionality = Column(Integer)

class tt_source_keywords(Base, BaseMixin):
    __tablename__ = "tt_source_keywords"
    keyword = Column(String(36), nullable=False)
    label_1 = Column(String(36))
    label_2 = Column(String(36))
    label_3 = Column(String(36))
    source = Column(FLOAT(precision=11, scale=2))
    emo_polarity = Column(Integer)
    is_stop_word = Column(Integer, default=0) #是否是停用词
    is_phrase = Column(Integer, default=0) # 是否是词组
    head_kw_id = Column(Integer)
    tail_kw_id = Column(Integer)
    single_kw_id = Column(Integer)
    confidence = Column(String(36), default="1")
    single_confidence = Column(String(36), default="1")
    head_confidence = Column(String(36), default="1") # affiliate_confidence
    tail_confidence = Column(String(36), default="1") # affiliate_confidence
    info = Column(String(255))
    directionality = Column(Integer)

class archon_tiktok_users(Base, BaseMixin):
    __tablename__ = "archon_tiktok_users"
    unique_id = Column(String(255), nullable=False)
    nickname = Column(String(255))
    avatar_larger = Column(String(255))
    avatar_src_url = Column(String(255))
    signature = Column(String(255))
    verified = Column(Integer)
    following_count = Column(Integer)
    follower_count = Column(Integer)
    heart_count = Column(Integer)
    video_count = Column(Integer)
    digg_count = Column(Integer)
    open_favorite = Column(Integer)
    private_account = Column(Integer)
    sec_uid = Column(String(255))

class archon_tiktok_posts(Base, BaseMixin):
    __tablename__ = "archon_tiktok_posts"
    desc = Column(String(36), nullable=False, unique=True)
    created_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    video = Column(String(36), nullable=False, unique=True)
    video_src_url = Column(String(36), nullable=False, unique=True)
    video_cover_url = Column(String(36), nullable=False, unique=True)
    author_id = Column(Integer, nullable=False, unique=True)
    author_unique_id = Column(String(36), nullable=False, unique=True)
    author = Column(String(36), nullable=False, unique=True)
    author_avatar_url = Column(String(36), nullable=False, unique=True)
    music = Column(String(36), nullable=False, unique=True)
    challenges = Column(String(36), nullable=False, unique=True)
    stats = Column(String(36), nullable=False, unique=True)
    duet_info = Column(String(36), nullable=False, unique=True)
    text_extra = Column(String(36), nullable=False, unique=True)
    for_friend = Column(Integer, nullable=False, unique=True)
    private_item = Column(Integer, nullable=False, unique=True)
    author_stats = Column(String(36), nullable=False, unique=True)
    duet_enabled = Column(Integer, nullable=False, unique=True)
    stitch_enabled = Column(Integer, nullable=False, unique=True)
    share_enabled = Column(Integer, nullable=False, unique=True)
    stickers_on_item = Column(String(36), nullable=False, unique=True)
    effect_stickers = Column(String(36), nullable=False, unique=True)
    is_ad = Column(Integer, nullable=False, unique=True)
    video_status = Column(Integer, nullable=False, unique=True)

class archon_tiktok_comments(Base, BaseMixin):
    __tablename__ = "archon_tiktok_comments"
    text = Column(String(255), nullable=False, unique=True)
    created_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    aweme_id = Column(String(36), nullable=False, unique=True)
    digg_count = Column(Integer, nullable=False, unique=True)
    status = Column(Integer, nullable=False, unique=True)
    user_id = Column(Integer, nullable=False, unique=True)
    user_unique_id = Column(String(36), nullable=False, unique=True)
    user = Column(String(36), nullable=False, unique=True)
    user_avatar_url = Column(String(36), nullable=False, unique=True)
    reply_comment = Column(String(36), nullable=False, unique=True)
    text_extra = Column(String(36), nullable=False, unique=True)
    is_author_digged = Column(Integer, nullable=False, unique=True)
    author_pin = Column(Integer, nullable=False, unique=True)
    reply_comment_total = Column(Integer, nullable=False, unique=True)
    reply_to_reply_id = Column(Integer, nullable=False, unique=True)
    reply_id = Column(Integer, nullable=False, unique=True)




if __name__ == "__main__":
    # 创建表的原子操作
    # Base.metadata.create_all(engine)

    pass