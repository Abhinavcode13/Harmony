from config.harmony_demo.indicator_groups.yellow_fever import YELLOW_FEVER_GROUPS
from data.aqt_datasources import build_data_source

GROUP_DEFINITIONS = []
GROUP_DEFINITIONS.extend(YELLOW_FEVER_GROUPS)

VALID_FIELDS = set()
for group in GROUP_DEFINITIONS:
    for ind in group['indicators']:
        VALID_FIELDS.add(ind['id'])

# Map indicator id to indicator name. Useful after requesting indicator ids from druid.
ID_LOOKUP = {
    val['id']: val for group in GROUP_DEFINITIONS for val in group['indicators']
}

DATA_SOURCES = []

for group in GROUP_DEFINITIONS:
    DATA_SOURCES.append(
        build_data_source(group['groupId'], group['groupText'], [group])
    )

REMOVED_INDICATORS = []
