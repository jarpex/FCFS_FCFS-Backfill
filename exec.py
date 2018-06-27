#! /usr/bin/env python3
while True:
        mode = input('FCFS or Backfill. For exit print :q! ')
        if mode != 'FCFS':
                if mode != 'Backfill':
                        if mode != ':q!':
                                print('Error.')
                        else:   
                                break
                else:
                        import FCFS_Backfill_NumPy
        else:
                import FCFS_NumPy