from slack_sdk.models.blocks import DataVisualizationBlock


def example01() -> DataVisualizationBlock:
    """
    Displays data visually in pie, bar, area, or line chart formats.
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
    An area chart comparing multiple series.
    """
    block = DataVisualizationBlock(
        title="Daily Active Users",
        chart={
            "type": "area",
            "series": [
                {
                    "name": "Pied Piper Free Tier",
                    "data": [
                        {"label": "Mon", "value": 12000},
                        {"label": "Tues", "value": 13500},
                        {"label": "Wed", "value": 15200},
                        {"label": "Thurs", "value": 14800},
                        {"label": "Fri", "value": 16400},
                    ],
                },
                {
                    "name": "Pied Piper Paid Tier",
                    "data": [
                        {"label": "Mon", "value": 4500},
                        {"label": "Tues", "value": 4800},
                        {"label": "Wed", "value": 5100},
                        {"label": "Thurs", "value": 5600},
                        {"label": "Fri", "value": 6200},
                    ],
                },
            ],
            "axis_config": {
                "categories": ["Mon", "Tues", "Wed", "Thur", "Fri"],
                "x_label": "Day",
                "y_label": "Users",
            },
        },
    )
    return block


def example04() -> DataVisualizationBlock:
    """
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
                        {"label": "Week 1", "value": 32000},
                        {"label": "Week 2", "value": 35000},
                        {"label": "Week 3", "value": 29000},
                        {"label": "Week 4", "value": 41000},
                        {"label": "Week 5", "value": 45000},
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
