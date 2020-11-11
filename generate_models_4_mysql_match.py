# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Enum, Float, LargeBinary, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, CHAR, ENUM, INTEGER, LONGBLOB, MEDIUMBLOB, MEDIUMTEXT, SET, SMALLINT, TEXT, TIME, TIMESTAMP, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ColumnsPriv(Base):
    __tablename__ = 'columns_priv'
    __table_args__ = {'comment': 'Column privileges'}

    Host = Column(CHAR(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Db = Column(CHAR(64, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    User = Column(CHAR(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Table_name = Column(CHAR(64, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Column_name = Column(CHAR(64, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Timestamp = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    Column_priv = Column(SET('Select', 'Insert', 'Update', 'References'), nullable=False, server_default=text("''"))


class Db(Base):
    __tablename__ = 'db'
    __table_args__ = {'comment': 'Database privileges'}

    Host = Column(CHAR(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Db = Column(CHAR(64, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    User = Column(CHAR(32, 'utf8_bin'), primary_key=True, nullable=False, index=True, server_default=text("''"))
    Select_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Insert_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Update_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Delete_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Create_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Drop_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Grant_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    References_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Index_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Alter_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Create_tmp_table_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Lock_tables_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Create_view_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Show_view_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Create_routine_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Alter_routine_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Execute_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Event_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Trigger_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))


class EngineCost(Base):
    __tablename__ = 'engine_cost'

    engine_name = Column(String(64), primary_key=True, nullable=False)
    device_type = Column(INTEGER(11), primary_key=True, nullable=False)
    cost_name = Column(String(64), primary_key=True, nullable=False)
    cost_value = Column(Float)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    comment = Column(String(1024))


class Event(Base):
    __tablename__ = 'event'
    __table_args__ = {'comment': 'Events'}

    db = Column(CHAR(64), primary_key=True, nullable=False, server_default=text("''"))
    name = Column(CHAR(64), primary_key=True, nullable=False, server_default=text("''"))
    body = Column(LONGBLOB, nullable=False)
    definer = Column(CHAR(93), nullable=False, server_default=text("''"))
    execute_at = Column(DateTime)
    interval_value = Column(INTEGER(11))
    interval_field = Column(Enum('YEAR', 'QUARTER', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'WEEK', 'SECOND', 'MICROSECOND', 'YEAR_MONTH', 'DAY_HOUR', 'DAY_MINUTE', 'DAY_SECOND', 'HOUR_MINUTE', 'HOUR_SECOND', 'MINUTE_SECOND', 'DAY_MICROSECOND', 'HOUR_MICROSECOND', 'MINUTE_MICROSECOND', 'SECOND_MICROSECOND'))
    created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    modified = Column(TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    last_executed = Column(DateTime)
    starts = Column(DateTime)
    ends = Column(DateTime)
    status = Column(Enum('ENABLED', 'DISABLED', 'SLAVESIDE_DISABLED'), nullable=False, server_default=text("'ENABLED'"))
    on_completion = Column(Enum('DROP', 'PRESERVE'), nullable=False, server_default=text("'DROP'"))
    sql_mode = Column(SET('REAL_AS_FLOAT', 'PIPES_AS_CONCAT', 'ANSI_QUOTES', 'IGNORE_SPACE', 'NOT_USED', 'ONLY_FULL_GROUP_BY', 'NO_UNSIGNED_SUBTRACTION', 'NO_DIR_IN_CREATE', 'POSTGRESQL', 'ORACLE', 'MSSQL', 'DB2', 'MAXDB', 'NO_KEY_OPTIONS', 'NO_TABLE_OPTIONS', 'NO_FIELD_OPTIONS', 'MYSQL323', 'MYSQL40', 'ANSI', 'NO_AUTO_VALUE_ON_ZERO', 'NO_BACKSLASH_ESCAPES', 'STRICT_TRANS_TABLES', 'STRICT_ALL_TABLES', 'NO_ZERO_IN_DATE', 'NO_ZERO_DATE', 'INVALID_DATES', 'ERROR_FOR_DIVISION_BY_ZERO', 'TRADITIONAL', 'NO_AUTO_CREATE_USER', 'HIGH_NOT_PRECEDENCE', 'NO_ENGINE_SUBSTITUTION', 'PAD_CHAR_TO_FULL_LENGTH'), nullable=False, server_default=text("''"))
    comment = Column(CHAR(64), nullable=False, server_default=text("''"))
    originator = Column(INTEGER(10), nullable=False)
    time_zone = Column(CHAR(64), nullable=False, server_default=text("'SYSTEM'"))
    character_set_client = Column(CHAR(32))
    collation_connection = Column(CHAR(32))
    db_collation = Column(CHAR(32))
    body_utf8 = Column(LONGBLOB)


class Func(Base):
    __tablename__ = 'func'
    __table_args__ = {'comment': 'User defined functions'}

    name = Column(CHAR(64, 'utf8_bin'), primary_key=True, server_default=text("''"))
    ret = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    dl = Column(CHAR(128, 'utf8_bin'), nullable=False, server_default=text("''"))
    type = Column(ENUM('function', 'aggregate'), nullable=False)


t_general_log = Table(
    'general_log', metadata,
    Column('event_time', TIMESTAMP(fsp=6), nullable=False, server_default=text("CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)")),
    Column('user_host', MEDIUMTEXT, nullable=False),
    Column('thread_id', BIGINT(21), nullable=False),
    Column('server_id', INTEGER(10), nullable=False),
    Column('command_type', String(64), nullable=False),
    Column('argument', MEDIUMBLOB, nullable=False),
    comment='General log'
)


class GtidExecuted(Base):
    __tablename__ = 'gtid_executed'

    source_uuid = Column(CHAR(36), primary_key=True, nullable=False, comment='uuid of the source where the transaction was originally executed.')
    interval_start = Column(BIGINT(20), primary_key=True, nullable=False, comment='First number of interval.')
    interval_end = Column(BIGINT(20), nullable=False, comment='Last number of interval.')


class HelpCategory(Base):
    __tablename__ = 'help_category'
    __table_args__ = {'comment': 'help categories'}

    help_category_id = Column(SMALLINT(5), primary_key=True)
    name = Column(CHAR(64), nullable=False, unique=True)
    parent_category_id = Column(SMALLINT(5))
    url = Column(Text, nullable=False)


class HelpKeyword(Base):
    __tablename__ = 'help_keyword'
    __table_args__ = {'comment': 'help keywords'}

    help_keyword_id = Column(INTEGER(10), primary_key=True)
    name = Column(CHAR(64), nullable=False, unique=True)


class HelpRelation(Base):
    __tablename__ = 'help_relation'
    __table_args__ = {'comment': 'keyword-topic relation'}

    help_topic_id = Column(INTEGER(10), primary_key=True, nullable=False)
    help_keyword_id = Column(INTEGER(10), primary_key=True, nullable=False)


class HelpTopic(Base):
    __tablename__ = 'help_topic'
    __table_args__ = {'comment': 'help topics'}

    help_topic_id = Column(INTEGER(10), primary_key=True)
    name = Column(CHAR(64), nullable=False, unique=True)
    help_category_id = Column(SMALLINT(5), nullable=False)
    description = Column(Text, nullable=False)
    example = Column(Text, nullable=False)
    url = Column(Text, nullable=False)


class InnodbIndexStat(Base):
    __tablename__ = 'innodb_index_stats'

    database_name = Column(String(64, 'utf8_bin'), primary_key=True, nullable=False)
    table_name = Column(String(199, 'utf8_bin'), primary_key=True, nullable=False)
    index_name = Column(String(64, 'utf8_bin'), primary_key=True, nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    stat_name = Column(String(64, 'utf8_bin'), primary_key=True, nullable=False)
    stat_value = Column(BIGINT(20), nullable=False)
    sample_size = Column(BIGINT(20))
    stat_description = Column(String(1024, 'utf8_bin'), nullable=False)


class InnodbTableStat(Base):
    __tablename__ = 'innodb_table_stats'

    database_name = Column(String(64, 'utf8_bin'), primary_key=True, nullable=False)
    table_name = Column(String(199, 'utf8_bin'), primary_key=True, nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    n_rows = Column(BIGINT(20), nullable=False)
    clustered_index_size = Column(BIGINT(20), nullable=False)
    sum_of_other_index_sizes = Column(BIGINT(20), nullable=False)


class NdbBinlogIndex(Base):
    __tablename__ = 'ndb_binlog_index'

    Position = Column(BIGINT(20), nullable=False)
    File = Column(String(255), nullable=False)
    epoch = Column(BIGINT(20), primary_key=True, nullable=False)
    inserts = Column(INTEGER(10), nullable=False)
    updates = Column(INTEGER(10), nullable=False)
    deletes = Column(INTEGER(10), nullable=False)
    schemaops = Column(INTEGER(10), nullable=False)
    orig_server_id = Column(INTEGER(10), primary_key=True, nullable=False)
    orig_epoch = Column(BIGINT(20), primary_key=True, nullable=False)
    gci = Column(INTEGER(10), nullable=False)
    next_position = Column(BIGINT(20), nullable=False)
    next_file = Column(String(255), nullable=False)


class Plugin(Base):
    __tablename__ = 'plugin'
    __table_args__ = {'comment': 'MySQL plugins'}

    name = Column(String(64), primary_key=True, server_default=text("''"))
    dl = Column(String(128), nullable=False, server_default=text("''"))


class Proc(Base):
    __tablename__ = 'proc'
    __table_args__ = {'comment': 'Stored Procedures'}

    db = Column(CHAR(64), primary_key=True, nullable=False, server_default=text("''"))
    name = Column(CHAR(64), primary_key=True, nullable=False, server_default=text("''"))
    type = Column(Enum('FUNCTION', 'PROCEDURE'), primary_key=True, nullable=False)
    specific_name = Column(CHAR(64), nullable=False, server_default=text("''"))
    language = Column(Enum('SQL'), nullable=False, server_default=text("'SQL'"))
    sql_data_access = Column(Enum('CONTAINS_SQL', 'NO_SQL', 'READS_SQL_DATA', 'MODIFIES_SQL_DATA'), nullable=False, server_default=text("'CONTAINS_SQL'"))
    is_deterministic = Column(Enum('YES', 'NO'), nullable=False, server_default=text("'NO'"))
    security_type = Column(Enum('INVOKER', 'DEFINER'), nullable=False, server_default=text("'DEFINER'"))
    param_list = Column(LargeBinary, nullable=False)
    returns = Column(LONGBLOB, nullable=False)
    body = Column(LONGBLOB, nullable=False)
    definer = Column(CHAR(93), nullable=False, server_default=text("''"))
    created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    modified = Column(TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    sql_mode = Column(SET('REAL_AS_FLOAT', 'PIPES_AS_CONCAT', 'ANSI_QUOTES', 'IGNORE_SPACE', 'NOT_USED', 'ONLY_FULL_GROUP_BY', 'NO_UNSIGNED_SUBTRACTION', 'NO_DIR_IN_CREATE', 'POSTGRESQL', 'ORACLE', 'MSSQL', 'DB2', 'MAXDB', 'NO_KEY_OPTIONS', 'NO_TABLE_OPTIONS', 'NO_FIELD_OPTIONS', 'MYSQL323', 'MYSQL40', 'ANSI', 'NO_AUTO_VALUE_ON_ZERO', 'NO_BACKSLASH_ESCAPES', 'STRICT_TRANS_TABLES', 'STRICT_ALL_TABLES', 'NO_ZERO_IN_DATE', 'NO_ZERO_DATE', 'INVALID_DATES', 'ERROR_FOR_DIVISION_BY_ZERO', 'TRADITIONAL', 'NO_AUTO_CREATE_USER', 'HIGH_NOT_PRECEDENCE', 'NO_ENGINE_SUBSTITUTION', 'PAD_CHAR_TO_FULL_LENGTH'), nullable=False, server_default=text("''"))
    comment = Column(TEXT, nullable=False)
    character_set_client = Column(CHAR(32))
    collation_connection = Column(CHAR(32))
    db_collation = Column(CHAR(32))
    body_utf8 = Column(LONGBLOB)


class ProcsPriv(Base):
    __tablename__ = 'procs_priv'
    __table_args__ = {'comment': 'Procedure privileges'}

    Host = Column(CHAR(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Db = Column(CHAR(64, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    User = Column(CHAR(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Routine_name = Column(CHAR(64), primary_key=True, nullable=False, server_default=text("''"))
    Routine_type = Column(ENUM('FUNCTION', 'PROCEDURE'), primary_key=True, nullable=False)
    Grantor = Column(CHAR(93, 'utf8_bin'), nullable=False, index=True, server_default=text("''"))
    Proc_priv = Column(SET('Execute', 'Alter Routine', 'Grant'), nullable=False, server_default=text("''"))
    Timestamp = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class ProxiesPriv(Base):
    __tablename__ = 'proxies_priv'
    __table_args__ = {'comment': 'User proxy privileges'}

    Host = Column(CHAR(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    User = Column(CHAR(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Proxied_host = Column(CHAR(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Proxied_user = Column(CHAR(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    With_grant = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    Grantor = Column(CHAR(93, 'utf8_bin'), nullable=False, index=True, server_default=text("''"))
    Timestamp = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class ServerCost(Base):
    __tablename__ = 'server_cost'

    cost_name = Column(String(64), primary_key=True)
    cost_value = Column(Float)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    comment = Column(String(1024))


class Server(Base):
    __tablename__ = 'servers'
    __table_args__ = {'comment': 'MySQL Foreign Servers table'}

    Server_name = Column(CHAR(64), primary_key=True, server_default=text("''"))
    Host = Column(CHAR(64), nullable=False, server_default=text("''"))
    Db = Column(CHAR(64), nullable=False, server_default=text("''"))
    Username = Column(CHAR(64), nullable=False, server_default=text("''"))
    Password = Column(CHAR(64), nullable=False, server_default=text("''"))
    Port = Column(INTEGER(4), nullable=False, server_default=text("'0'"))
    Socket = Column(CHAR(64), nullable=False, server_default=text("''"))
    Wrapper = Column(CHAR(64), nullable=False, server_default=text("''"))
    Owner = Column(CHAR(64), nullable=False, server_default=text("''"))


class SlaveMasterInfo(Base):
    __tablename__ = 'slave_master_info'
    __table_args__ = {'comment': 'Master Information'}

    Number_of_lines = Column(INTEGER(10), nullable=False, comment='Number of lines in the file.')
    Master_log_name = Column(TEXT, nullable=False, comment='The name of the master binary log currently being read from the master.')
    Master_log_pos = Column(BIGINT(20), nullable=False, comment='The master log position of the last read event.')
    Host = Column(CHAR(64), comment='The host name of the master.')
    User_name = Column(TEXT, comment='The user name used to connect to the master.')
    User_password = Column(TEXT, comment='The password used to connect to the master.')
    Port = Column(INTEGER(10), nullable=False, comment='The network port used to connect to the master.')
    Connect_retry = Column(INTEGER(10), nullable=False, comment='The period (in seconds) that the slave will wait before trying to reconnect to the master.')
    Enabled_ssl = Column(TINYINT(1), nullable=False, comment='Indicates whether the server supports SSL connections.')
    Ssl_ca = Column(TEXT, comment='The file used for the Certificate Authority (CA) certificate.')
    Ssl_capath = Column(TEXT, comment='The path to the Certificate Authority (CA) certificates.')
    Ssl_cert = Column(TEXT, comment='The name of the SSL certificate file.')
    Ssl_cipher = Column(TEXT, comment='The name of the cipher in use for the SSL connection.')
    Ssl_key = Column(TEXT, comment='The name of the SSL key file.')
    Ssl_verify_server_cert = Column(TINYINT(1), nullable=False, comment='Whether to verify the server certificate.')
    Heartbeat = Column(Float, nullable=False)
    Bind = Column(TEXT, comment='Displays which interface is employed when connecting to the MySQL server')
    Ignored_server_ids = Column(TEXT, comment='The number of server IDs to be ignored, followed by the actual server IDs')
    Uuid = Column(TEXT, comment='The master server uuid.')
    Retry_count = Column(BIGINT(20), nullable=False, comment='Number of reconnect attempts, to the master, before giving up.')
    Ssl_crl = Column(TEXT, comment='The file used for the Certificate Revocation List (CRL)')
    Ssl_crlpath = Column(TEXT, comment='The path used for Certificate Revocation List (CRL) files')
    Enabled_auto_position = Column(TINYINT(1), nullable=False, comment='Indicates whether GTIDs will be used to retrieve events from the master.')
    Channel_name = Column(CHAR(64), primary_key=True, comment='The channel on which the slave is connected to a source. Used in Multisource Replication')
    Tls_version = Column(TEXT, comment='Tls version')


class SlaveRelayLogInfo(Base):
    __tablename__ = 'slave_relay_log_info'
    __table_args__ = {'comment': 'Relay Log Information'}

    Number_of_lines = Column(INTEGER(10), nullable=False, comment='Number of lines in the file or rows in the table. Used to version table definitions.')
    Relay_log_name = Column(TEXT, nullable=False, comment='The name of the current relay log file.')
    Relay_log_pos = Column(BIGINT(20), nullable=False, comment='The relay log position of the last executed event.')
    Master_log_name = Column(TEXT, nullable=False, comment='The name of the master binary log file from which the events in the relay log file were read.')
    Master_log_pos = Column(BIGINT(20), nullable=False, comment='The master log position of the last executed event.')
    Sql_delay = Column(INTEGER(11), nullable=False, comment='The number of seconds that the slave must lag behind the master.')
    Number_of_workers = Column(INTEGER(10), nullable=False)
    Id = Column(INTEGER(10), nullable=False, comment='Internal Id that uniquely identifies this record.')
    Channel_name = Column(CHAR(64), primary_key=True, comment='The channel on which the slave is connected to a source. Used in Multisource Replication')


class SlaveWorkerInfo(Base):
    __tablename__ = 'slave_worker_info'
    __table_args__ = {'comment': 'Worker Information'}

    Id = Column(INTEGER(10), primary_key=True, nullable=False)
    Relay_log_name = Column(TEXT, nullable=False)
    Relay_log_pos = Column(BIGINT(20), nullable=False)
    Master_log_name = Column(TEXT, nullable=False)
    Master_log_pos = Column(BIGINT(20), nullable=False)
    Checkpoint_relay_log_name = Column(TEXT, nullable=False)
    Checkpoint_relay_log_pos = Column(BIGINT(20), nullable=False)
    Checkpoint_master_log_name = Column(TEXT, nullable=False)
    Checkpoint_master_log_pos = Column(BIGINT(20), nullable=False)
    Checkpoint_seqno = Column(INTEGER(10), nullable=False)
    Checkpoint_group_size = Column(INTEGER(10), nullable=False)
    Checkpoint_group_bitmap = Column(LargeBinary, nullable=False)
    Channel_name = Column(CHAR(64), primary_key=True, nullable=False, comment='The channel on which the slave is connected to a source. Used in Multisource Replication')


t_slow_log = Table(
    'slow_log', metadata,
    Column('start_time', TIMESTAMP(fsp=6), nullable=False, server_default=text("CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)")),
    Column('user_host', MEDIUMTEXT, nullable=False),
    Column('query_time', TIME(fsp=6), nullable=False),
    Column('lock_time', TIME(fsp=6), nullable=False),
    Column('rows_sent', INTEGER(11), nullable=False),
    Column('rows_examined', INTEGER(11), nullable=False),
    Column('db', String(512), nullable=False),
    Column('last_insert_id', INTEGER(11), nullable=False),
    Column('insert_id', INTEGER(11), nullable=False),
    Column('server_id', INTEGER(10), nullable=False),
    Column('sql_text', MEDIUMBLOB, nullable=False),
    Column('thread_id', BIGINT(21), nullable=False),
    comment='Slow log'
)


class TablesPriv(Base):
    __tablename__ = 'tables_priv'
    __table_args__ = {'comment': 'Table privileges'}

    Host = Column(CHAR(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Db = Column(CHAR(64, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    User = Column(CHAR(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Table_name = Column(CHAR(64, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Grantor = Column(CHAR(93, 'utf8_bin'), nullable=False, index=True, server_default=text("''"))
    Timestamp = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    Table_priv = Column(SET('Select', 'Insert', 'Update', 'Delete', 'Create', 'Drop', 'Grant', 'References', 'Index', 'Alter', 'Create View', 'Show view', 'Trigger'), nullable=False, server_default=text("''"))
    Column_priv = Column(SET('Select', 'Insert', 'Update', 'References'), nullable=False, server_default=text("''"))


class TimeZone(Base):
    __tablename__ = 'time_zone'
    __table_args__ = {'comment': 'Time zones'}

    Time_zone_id = Column(INTEGER(10), primary_key=True)
    Use_leap_seconds = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))


class TimeZoneLeapSecond(Base):
    __tablename__ = 'time_zone_leap_second'
    __table_args__ = {'comment': 'Leap seconds information for time zones'}

    Transition_time = Column(BIGINT(20), primary_key=True)
    Correction = Column(INTEGER(11), nullable=False)


class TimeZoneName(Base):
    __tablename__ = 'time_zone_name'
    __table_args__ = {'comment': 'Time zone names'}

    Name = Column(CHAR(64), primary_key=True)
    Time_zone_id = Column(INTEGER(10), nullable=False)


class TimeZoneTransition(Base):
    __tablename__ = 'time_zone_transition'
    __table_args__ = {'comment': 'Time zone transitions'}

    Time_zone_id = Column(INTEGER(10), primary_key=True, nullable=False)
    Transition_time = Column(BIGINT(20), primary_key=True, nullable=False)
    Transition_type_id = Column(INTEGER(10), nullable=False)


class TimeZoneTransitionType(Base):
    __tablename__ = 'time_zone_transition_type'
    __table_args__ = {'comment': 'Time zone transition types'}

    Time_zone_id = Column(INTEGER(10), primary_key=True, nullable=False)
    Transition_type_id = Column(INTEGER(10), primary_key=True, nullable=False)
    Offset = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    Is_DST = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    Abbreviation = Column(CHAR(8), nullable=False, server_default=text("''"))


class Tpoint(Base):
    __tablename__ = 'tpoint'

    row_id = Column(INTEGER(10), primary_key=True)
    location_id = Column(CHAR(20), nullable=False)
    province_name = Column(VARCHAR(255), nullable=False)
    city_name = Column(VARCHAR(255), nullable=False)
    district_name = Column(VARCHAR(255))
    town_name = Column(VARCHAR(255))
    location_name = Column(VARCHAR(255), nullable=False)
    address = Column(VARCHAR(255), nullable=False)
    longitude = Column(Float(255, True), nullable=False)
    latitude = Column(Float(255, True), nullable=False)


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'comment': 'Users and global privileges'}

    Host = Column(CHAR(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    User = Column(CHAR(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=text("''"))
    Select_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Insert_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Update_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Delete_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Create_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Drop_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Reload_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Shutdown_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Process_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    File_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Grant_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    References_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Index_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Alter_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Show_db_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Super_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Create_tmp_table_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Lock_tables_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Execute_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Repl_slave_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Repl_client_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Create_view_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Show_view_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Create_routine_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Alter_routine_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Create_user_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Event_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Trigger_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    Create_tablespace_priv = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    ssl_type = Column(ENUM('', 'ANY', 'X509', 'SPECIFIED'), nullable=False, server_default=text("''"))
    ssl_cipher = Column(LargeBinary, nullable=False)
    x509_issuer = Column(LargeBinary, nullable=False)
    x509_subject = Column(LargeBinary, nullable=False)
    max_questions = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    max_updates = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    max_connections = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    max_user_connections = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    plugin = Column(CHAR(64, 'utf8_bin'), nullable=False, server_default=text("'mysql_native_password'"))
    authentication_string = Column(Text(collation='utf8_bin'))
    password_expired = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
    password_last_changed = Column(TIMESTAMP)
    password_lifetime = Column(SMALLINT(5))
    account_locked = Column(ENUM('N', 'Y'), nullable=False, server_default=text("'N'"))
