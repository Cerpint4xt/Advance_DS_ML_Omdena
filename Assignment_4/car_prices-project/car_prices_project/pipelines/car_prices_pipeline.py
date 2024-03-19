# The following is the code added to a pipelines folder to schedule the process 

from dagster import solid, pipeline, schedules, ScheduleDefinition, daily_schedule, ModeDefinition
from datetime import datetime

@solid
def data_processing(context):
    # Your data processing code here
    pass

@pipeline(
    mode_defs=[ModeDefinition(name="default")]
)
def data_pipeline():
    data_processing()

daily_schedule = ScheduleDefinition(
    name="daily_schedule",
    cron_schedule="0 0 * * *",  # Run at midnight every day
    pipeline_name="data_pipeline",
    execution_timezone="UTC"
)

# This decorator registers the schedule with the repository containing the pipeline
@schedules
def define_schedules():
    return [daily_schedule]