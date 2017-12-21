from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..constants import WEEK10, WEEK16
from .crfs import crfs_w10, crfs_w16, crfs_unscheduled
from .requisitions import requisitions

# schedule for terminated participants.
schedule_w10 = Schedule(
    name='schedule',
    title='Ambition',
    onschedule_model='ambition_prn.onschedulew10',
    offschedule_model='ambition_prn.offschedulew10',
)

visit10 = Visit(
    code=WEEK10,
    title='Week 10',
    timepoint=10,
    rbase=relativedelta(weeks=10),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs_w10,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='5-day clinic',
    allow_unscheduled=False)

visit16 = Visit(
    code=WEEK16,
    title='Week 16',
    timepoint=16,
    rbase=relativedelta(weeks=16),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs_w16,
    crfs_unscheduled=crfs_unscheduled,
    facility_name='5-day clinic',
    requisitions_unscheduled=requisitions,
)

schedule_w10.add_visit(visit=visit10)
schedule_w10.add_visit(visit=visit16)
