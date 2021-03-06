#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import time

#call as gridmovie.py filename nx ny lx ly dt skip

filename = sys.argv[1]
nx = int(sys.argv[2])
ny = int(sys.argv[3])
lx = float(sys.argv[4])
ly = float(sys.argv[5])
dt = float(sys.argv[6])
skip = int(sys.argv[7])

raw = np.genfromtxt(filename)
sraw = raw.size
nt = raw.size/(nx+1)/(ny+1)

grid = np.zeros((nx+1,ny+1,nt))

n=0
for t in range(nt):
  for j in range(ny+1):
    for i in range(nx+1):
      grid[i,j,t]=raw[n]
      n=n+1


f = plt.figure()
a = f.gca()
f.show()
mesh = a.pcolormesh(grid[:,:,0].T)
cb = plt.colorbar(mesh, ax=a)
for t in range(0,nt-1,skip):
  a.clear()
  mesh = a.pcolormesh(grid[:,:,t].T)
  cb.update_bruteforce(mesh)
  f.suptitle('T = '+str(dt*t))
  f.canvas.draw()
  time.sleep(0.01)
