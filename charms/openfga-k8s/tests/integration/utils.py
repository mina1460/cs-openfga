import glob
import logging
from pathlib import Path
from typing import Dict

from juju.unit import Unit
from pytest_operator.plugin import OpsTest

LOGGER = logging.getLogger(__name__)


async def get_unit_by_name(unit_name: str, unit_index: str, unit_list: Dict[str, Unit]) -> Unit:
    return unit_list.get("{unitname}/{unitindex}".format(unitname=unit_name, unitindex=unit_index))


async def fetch_charm(ops_test: OpsTest, charm_name, path_to_charm) -> str:
    """Uses an existing charm in the directory or builds the charm if it doesn't exist."""
    LOGGER.info("Building charm...")
    try:
        charm_path = Path(get_local_charm(charm_name, path_to_charm)).resolve()
        LOGGER.info("Skipping charm build. Found existing charm.")
    except FileNotFoundError:
        charm_path = await ops_test.build_charm(path_to_charm)
    LOGGER.info("Charm path is: %s", charm_path)
    return charm_path


def get_local_charm(charm_name, path_to_charm):
    charm = glob.glob(str(Path(path_to_charm, charm_name).absolute()))
    if len(charm) != 1:
        raise FileNotFoundError(f"Found {len(charm)} file(s) with matching name.")
    return charm[0]
