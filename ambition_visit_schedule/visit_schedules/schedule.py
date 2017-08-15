from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from .crfs import (
    crfs_d5, crfs_d1, crfs_d3, crfs_d7, crfs_d10, crfs_d12, crfs_d14,
    crfs_w4, crfs_w6, crfs_w8, crfs_w10, crfs_w16, crfs_unscheduled)
from .requisitions import (requisitions, requisitions_d1, requisitions_d3,
                           requisitions_d7, requisitions_w4)

# schedule for new participants
schedule1 = Schedule(
    name='schedule1',
    title='Ambition',
    enrollment_model='ambition_subject.enrollment',
    disenrollment_model='ambition_subject.disenrollment',
)

visit0 = Visit(
    code='1000',
    title='Day 1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    crfs=crfs_d1,
    requisitions=requisitions_d1,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit1 = Visit(
    code='1003',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d3,
    crfs=crfs_d3,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit2 = Visit(
    code='1005',
    title='Day 5',
    timepoint=2,
    rbase=relativedelta(days=5),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d3,
    crfs=crfs_d5,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit3 = Visit(
    code='1007',
    title='Day 7',
    timepoint=3,
    rbase=relativedelta(days=7),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d7,
    crfs=crfs_d7,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit4 = Visit(
    code='1010',
    title='Day 10',
    timepoint=4,
    rbase=relativedelta(days=10),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d3,
    crfs=crfs_d10,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit5 = Visit(
    code='1012',
    title='Day 12',
    timepoint=5,
    rbase=relativedelta(days=12),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d3,
    crfs=crfs_d12,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit6 = Visit(
    code='1014',
    title='Day 14',
    timepoint=6,
    rbase=relativedelta(days=14),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_d7,
    crfs=crfs_d14,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit7 = Visit(
    code='1028',
    title='Week 4',
    timepoint=7,
    rbase=relativedelta(weeks=4),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_w4,
    crfs=crfs_w4,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit8 = Visit(
    code='1042',
    title='Week 6',
    timepoint=8,
    rbase=relativedelta(weeks=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs_w6,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit9 = Visit(
    code='1056',
    title='Week 8',
    timepoint=9,
    rbase=relativedelta(weeks=8),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs_w8,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit10 = Visit(
    code='1070',
    title='Week 10',
    timepoint=10,
    rbase=relativedelta(weeks=10),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs_w10,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

visit16 = Visit(
    code='1112',
    title='Week 16',
    timepoint=16,
    rbase=relativedelta(weeks=16),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs_w16,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions)

schedule1.add_visit(visit=visit0)
schedule1.add_visit(visit=visit1)
schedule1.add_visit(visit=visit2)
schedule1.add_visit(visit=visit3)
schedule1.add_visit(visit=visit4)
schedule1.add_visit(visit=visit5)
schedule1.add_visit(visit=visit6)
schedule1.add_visit(visit=visit7)
schedule1.add_visit(visit=visit8)
schedule1.add_visit(visit=visit9)
schedule1.add_visit(visit=visit10)
schedule1.add_visit(visit=visit16)
