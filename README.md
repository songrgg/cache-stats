# cache-stats
向监控宝提供缓存服务器状态查询API

# 配置

    [
      {
        "type": "redis",
        "name": "localhost-redis",
        "host": "localhost",
        "port": 6379
      },
      {
        "type": "memcached",
        "name": "localhost-memcache",
        "host": "localhost",
        "port": 11211
      }
    ]
    
# 查询
GET /cache-stats?name=localhost-redis返回redis状态  
GET /cache-stats?name=localhost-memcache返回memcache状态
