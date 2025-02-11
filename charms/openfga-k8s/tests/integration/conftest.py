import logging

import pytest_asyncio
from pytest_operator.plugin import OpsTest
from utils import fetch_charm

logger = logging.getLogger(__name__)


@pytest_asyncio.fixture(scope="module")
async def charm(ops_test: OpsTest):
    logger.info("Building local charm")
    charm = await fetch_charm(ops_test, "*.charm", ".")
    yield charm


@pytest_asyncio.fixture(scope="module")
async def test_charm(ops_test: OpsTest):
    logger.info("Building local test charm")
    test_charm = await fetch_charm(ops_test, "*.charm", "./tests/charms/openfga_requires/")
    yield test_charm
