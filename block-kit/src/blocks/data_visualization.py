from typing import Any, Dict, Optional, Set

from slack_sdk.models.blocks import Block


class DataVisualizationBlock(Block):
    """Displays data using a line, bar, area, or pie chart.
    https://docs.slack.dev/reference/block-kit/blocks/data-visualization-block

    The slack_sdk does not yet ship a typed class for this block, so this
    example defines one that mirrors the SDK convention.
    """

    type = "data_visualization"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union({"title", "chart"})

    def __init__(
        self,
        *,
        title: str,
        chart: Dict[str, Any],
        block_id: Optional[str] = None,
    ) -> None:
        """
        Args:
            title (required): A label describing the chart. Maximum 50 characters.
            chart (required): The chart payload. The type must be one of pie, bar,
                area, or line. Pie charts use a segments array, while bar, area, and
                line charts use a series array alongside an axis_config object.
            block_id: A unique identifier for a block. If not specified, a block_id
                will be generated. Maximum length for this field is 255 characters.
        """
        super().__init__(type=self.type, block_id=block_id)
        self.title = title
        self.chart = chart


def example01() -> DataVisualizationBlock:
    """
    Displays data using a pie chart.
    https://docs.slack.dev/reference/block-kit/blocks/data-visualization-block/

    A pie chart with labeled segments.
    """
    block = DataVisualizationBlock(
        title="My Favorite Candy Bars",
        chart={
            "type": "pie",
            "segments": [
                {"label": "Kit Kat", "value": 45},
                {"label": "Twix", "value": 28},
                {"label": "Crunch", "value": 18},
                {"label": "Milky Way", "value": 9},
            ],
        },
    )
    return block


def example02() -> DataVisualizationBlock:
    """
    Displays data using a bar chart.
    https://docs.slack.dev/reference/block-kit/blocks/data-visualization-block/

    A bar chart with a single series and axis configuration.
    """
    block = DataVisualizationBlock(
        title="My Favorite Pies by Percentage of Tastiness",
        chart={
            "type": "bar",
            "series": [
                {
                    "name": "Pies",
                    "data": [
                        {"label": "Strawberry Rhubarb", "value": 85},
                        {"label": "Pumpkin", "value": 70},
                        {"label": "Lemon Meringue", "value": 72},
                        {"label": "Blueberry", "value": 90},
                        {"label": "Key Lime", "value": 56},
                    ],
                }
            ],
            "axis_config": {
                "categories": [
                    "Strawberry Rhubarb",
                    "Pumpkin",
                    "Lemon Meringue",
                    "Blueberry",
                    "Key Lime",
                ],
                "x_label": "Pies",
                "y_label": "Percentage of Tastiness",
            },
        },
    )
    return block


def example03() -> DataVisualizationBlock:
    """
    Displays data using a line chart.
    https://docs.slack.dev/reference/block-kit/blocks/data-visualization-block/

    A line chart comparing multiple series over time.
    """
    block = DataVisualizationBlock(
        title="Weekly Paper Sales",
        chart={
            "type": "line",
            "series": [
                {
                    "name": "Dunder Mifflin Infinity Website",
                    "data": [
                        {"label": "Week 1", "value": 32000},
                        {"label": "Week 2", "value": 35000},
                        {"label": "Week 3", "value": 29000},
                        {"label": "Week 4", "value": 41000},
                        {"label": "Week 5", "value": 45000},
                    ],
                },
                {
                    "name": "Dunder Mifflin In-store",
                    "data": [
                        {"label": "Week 1", "value": 18000},
                        {"label": "Week 2", "value": 21000},
                        {"label": "Week 3", "value": 24000},
                        {"label": "Week 4", "value": 22000},
                        {"label": "Week 5", "value": 26000},
                    ],
                },
            ],
            "axis_config": {
                "categories": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"],
                "x_label": "Week",
                "y_label": "Paper Sales (USD)",
            },
        },
    )
    return block
