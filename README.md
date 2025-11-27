# 集成测试实践作业

## 作业内容
- 作业1：RESTful API接口测试
- 作业2：数据库集成测试
- 作业3：微服务组件集成测试
- 作业4：持续集成环境下的自动化测试

## 测试策略
采用 **三明治集成策略**：先测试API接口，再测试数据库交互，最后在CI环境中统一执行。

## 测试工具
- Postman：接口功能验证
- Python + pytest + requests：自动化接口测试
- mysql-connector-python：数据库集成测试
- GitHub Actions：持续集成自动化测试

## 执行步骤
```bash
# 安装依赖
pip install -r requirements.txt

# 运行所有测试
pytest -v

# 生成覆盖率报告
coverage run -m pytest
coverage report -m
coverage html
