from requests.adapters import HTTPAdapter
from requests_toolbelt.sessions import BaseUrlSession


class Http:
    def __init__(
            self,
            base_url: str = '',
            default_headers: dict = None,
            pool_connections: int = 10,
            pool_maxsize: int = 10,
            timeout: int = 15,
    ) -> None:
        self.__http = None
        # 基础信息
        self.__base_url = base_url
        self.__default_headers = default_headers
        self.__timeout = timeout
        # 连接池信息
        self.__pool_connections = pool_connections
        self.__pool_maxsize = pool_maxsize

    def create(self) -> BaseUrlSession:
        """创建HTTP会话"""
        self.__http = BaseUrlSession(self.__base_url)

        # 设置最大连接数
        adapters = HTTPAdapter(
            pool_connections=self.__pool_connections,
            pool_maxsize=self.__pool_maxsize
        )
        self.__http.mount('http://', adapters)
        self.__http.mount('https://', adapters)

        # 设置默认请求头
        self.__http.headers.update(self.__default_headers)

        # 设置超时时间
        self.__http.timeout = self.__timeout

        return self.__http
