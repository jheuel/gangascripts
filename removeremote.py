def removeLFNs_subjobs(job,sublist):
    ds = LHCbDataset()
    if type(job.backend)==Dirac:
        for sj in sublist:
            if job.subjobs(sj).status == 'completed':
              ds.extend(job.subjobs(sj).backend.getOutputDataLFNs())
        for lfn in ds:
            lfn.remove()
def removeLFNs(job):
    ds = LHCbDataset()
    if type(job.backend)==Dirac:
        for sj in job.subjobs:
            if sj.status == 'completed':
              ds.extend(sj.backend.getOutputDataLFNs())
        for lfn in ds:
            lfn.remove()

def removeJobAndData(job):
    removeLFNs(job)
    job.remove()

def move_lfn_to_eos(lfn):
  lfn.replicate('CERN-USER')
  reps = lfn.getReplicas()
  if 'CERN-USER' in reps.keys():
     for key in reps.keys():
        if key != 'CERN-USER':
            lfn.removeReplica(key)

def move_job_to_eos(job):
    ds = LHCbDataset()
    if type(job.backend)==Dirac:
        for sj in job.subjobs:
            if sj.status == 'completed':
              ds.extend(sj.backend.getOutputDataLFNs())
        for lfn in ds:
            move_lfn_to_eos(lfn)