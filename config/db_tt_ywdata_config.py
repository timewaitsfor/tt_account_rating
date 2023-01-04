from config.db_config import *
import contextlib

# mg tt_data 数据库读取
tt_ywdata_engine = create_engine('mysql+pymysql://root:tt_analysis!1234@124.70.42.69:3306/tt_ywdata?charset=utf8', echo=False)
# mg_engine = create_engine('mysql+pymysql://root:1122@localhost:3306/tt_data?charset=utf8', echo=False)
TT_YWData_Session = sessionmaker(bind=tt_ywdata_engine)
TT_YWData_Base = declarative_base(tt_ywdata_engine)

@contextlib.contextmanager
def get_tt_ywdata_session():
    s = TT_YWData_Session()
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        if "Duplicate entry"  not in str(e):
            print(e)
        else:
            print(e)
    finally:
        s.close()

class tt_ywdata_content(TT_YWData_Base):
    __tablename__ = "content"
    id = Column(BIGINT, primary_key=True)
    author = Column(String(255), nullable=False)
    author_id = Column(BIGINT)
    tt_text = Column(String(4096))
    tt_type = Column(Integer, nullable=False)
    clean_txt = Column(String(4096))
    publish_date = Column(Integer)
    save_time = Column(Integer)
    video_id = Column(BIGINT, nullable=False)
    video_author = Column(String(4096), nullable=False)
    video_author_id = Column(BIGINT, nullable=False)
    video_src_url = Column(Text)
    music_playUrl = Column(Text)
    music_title = Column(String(2000))
    stats_diggCount = Column(BIGINT)
    stats_shareCount = Column(BIGINT)
    stats_commentCount = Column(BIGINT)
    stats_playCount = Column(BIGINT)
    created_at = Column(BIGINT)
    updated_at = Column(BIGINT)
    ocr_result = Column(Text)
    face_result = Column(Text)
    ocr_flag = Column(Integer)
    face_flag = Column(Integer)
    task_id = Column(BIGINT)
    bert_score = Column(Float)
    cluster = Column(JSON)


class tt_ywdata_author_analysed(TT_YWData_Base):
    __tablename__ = "author_analysed"
    author = Column(String(255), primary_key=True, nullable=False)
    author_id = Column(BIGINT)
    tt_number = Column(Integer)
    tt_zh_number = Column(Integer)
    cluster_bad_number = Column(Integer)
    bert_bad_number = Column(Integer)
    keyword_bad_number = Column(Integer)
    desc = Column(String(128))
    save_time = Column(Integer)
    from_src = Column(String(128))
    score = Column(Integer)

class tt_ywdata_task(TT_YWData_Base):
    __tablename__ = "task"
    id = Column(BIGINT, nullable=False)
    value = Column(String(255), primary_key=True, nullable=False)
    type = Column(Integer, nullable=False)
    website = Column(String(255))
    d_flag = Column(Integer)
    get_flag = Column(Integer)
    exec_flag = Column(Integer)
    create_time = Column(BIGINT)
    start_time = Column(BIGINT)
    end_time = Column(BIGINT)
    update_time = Column(BIGINT)
    period_type = Column(Integer)
    period = Column(Integer)
    host = Column(String(255))
    image_state = Column(Integer)


class tt_ywdata_exp_author_analysed(TT_YWData_Base):
    __tablename__ = "exp_author_analysed"
    author = Column(String(255), primary_key=True, nullable=False)
    author_id = Column(BIGINT)
    tt_number = Column(Integer)
    tt_zh_number = Column(Integer)
    cluster_bad_number = Column(Integer)
    bert_bad_number = Column(Integer)
    keyword_bad_number = Column(Integer)
    desc = Column(String(128))
    save_time = Column(Integer)
    from_src = Column(String(128))
    score = Column(Integer)

class tt_ywdata_exp_content(TT_YWData_Base, BaseMixin):
    __tablename__ = "exp_content"
    id = Column(BIGINT, primary_key=True)
    author = Column(String(255), nullable=False)
    author_id = Column(BIGINT)
    tt_text = Column(String(4096))
    tt_type = Column(Integer, nullable=False)
    clean_txt = Column(String(4096))
    publish_date = Column(Integer)
    save_time = Column(Integer)
    video_id = Column(BIGINT, nullable=False)
    video_author = Column(String(4096), nullable=False)
    video_author_id = Column(BIGINT, nullable=False)
    video_src_url = Column(Text)
    music_playUrl = Column(Text)
    music_title = Column(String(2000))
    stats_diggCount = Column(BIGINT)
    stats_shareCount = Column(BIGINT)
    stats_commentCount = Column(BIGINT)
    stats_playCount = Column(BIGINT)
    created_at = Column(BIGINT)
    updated_at = Column(BIGINT)
    ocr_result = Column(Text)
    face_result = Column(Text)
    ocr_flag = Column(Integer)
    face_flag = Column(Integer)
    task_id = Column(BIGINT)
    bert_score = Column(Float)
    cluster = Column(JSON)


if __name__ == "__main__":
    # 创建表的原子操作
    TT_YWData_Base.metadata.create_all(tt_ywdata_engine)

    # with get_tt_ywdata_session() as s:
    #     s.add(tt_ywdata_content(id=19921122, author='mo', tt_type=1122, video_id=11221122))

    pass