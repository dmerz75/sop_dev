#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time

import numpy as np
from glob import glob
my_dir = os.path.abspath(os.path.dirname(__file__))


#  ---------------------------------------------------------  #
#  functions                                                  #
#  ---------------------------------------------------------  #
# mpl_moving_average
# mpl_forcequench
# mpl_worm

#  ---------------------------------------------------------  #
#  Start matplotlib (1/4)                                     #
#  ---------------------------------------------------------  #
import matplotlib
# default - Qt5Agg
# print matplotlib.rcsetup.all_backends
# matplotlib.use('GTKAgg')
# matplotlib.use('TkAgg')
print 'backend:',matplotlib.get_backend()
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
fig = plt.figure(0)

gs = GridSpec(1,1)
ax1 = plt.subplot(gs[0,:])
# ax2 = plt.subplot(gs[1,:-1])

#  ---------------------------------------------------------  #
#  Import Data! (2/4)                                         #
#  ---------------------------------------------------------  #
result_type = 'fene' # sop | sopnucleo | gsop | namd
plot_type = 'potential' # fe | tension | rmsd | rdf
data_name = 'general1' # seed #
# save_fig(0,'fig','%s_%s_%s' % (result_type,plot_type,data_name))
combined_name = '%s_%s_%s' % (result_type, plot_type, data_name)

#  ---------------------------------------------------------  #
#  mpl_myargs_begin                                           #
#  ---------------------------------------------------------  #
import argparse

def parse_arguments():
    ''' Parse script's arguments.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-o","--option",help="select None,publish,show")
    args = vars(parser.parse_args())
    return args

args = parse_arguments()
''' Options:
args['makefile']
args['procs']
args['node'])
'''
option = args['option']


#  ---------------------------------------------------------  #
#  Import Data! (3/4)                                         #
#  ---------------------------------------------------------  #

# Lennard-Jones
# r0 = 0.480
# xlj = np.linspace(0.466,1.3,200)
# V = 4 * 1.5 * ((r0 / xlj) ** 12 - (r0 / xlj) ** 6)
# plt.plot(xlj,V,'b-')

# xlj = np.linspace(0.466,0.54,200)
# V = 4 * 1.5 * ((r0 / xlj) ** 12 - (r0 / xlj) ** 6)
# plt.plot(xlj,V,'r-')

# V = 4 * 1.68 * ((r0 / xlj) ** 12 - (r0 / xlj) ** 6)
# plt.plot(xlj,V,'r--')


# fene
r0 = 0.380
r = np.linspace(0.330,0.430,201)
k = 0.05 # 0.05

numerator = 1 - ((r - r0) ** 2)
prefactor = 0.5 * k * r0 ** 2
r02 = r0 ** 2
take_log = numerator / r02


# V = 1000 * ( 1000 * prefactor * np.log(take_log) - 6.98)
V = 1000 * ((( 1000 * prefactor * np.log(take_log)) * -1) + 0.0) + 6980.0
# V = (prefactor * np.log(take_log)) * 1000
print V
plt.plot(r,V,'k-',linewidth=7.0)

print 'r02',r02
print 'r',r
print 'num',numerator
print 'V',V


#  ---------------------------------------------------------  #
#  Make final adjustments: (4/4)                              #
#  mpl - available expansions                                 #
#  ---------------------------------------------------------  #
# matplotlib.rcParams[''] =
plt.subplots_adjust(left=0.24,right=0.940,top=0.920,bottom=0.170)
# font_prop_large = matplotlib.font_manager.FontProperties(size='large')
# fig.set_size_inches(9.0,5.1)
# for k in matplotlib.rcParams.keys():
#     print k
# dct_font = {'family':'sans-serif',
#             'weight':'normal',
#             'size'  :'28'}
# matplotlib.rc('font',**dct_font)
# matplotlib.rcParams['legend.frameon'] = False
# matplotlib.rcParams['figure.dpi'] = 900
# print matplotlib.rcParams['figure.dpi']

# mpl_label
# mpl_xy: set_xlim,set_ylim,xticks,yticks

plt.title("FENE")

ax1.set_xlim(0.329,0.431)
ax1.set_xlabel("r (nm)")
ax1.set_ylim(-7.2,0.2)
ax1.set_ylabel("Energy (kcal/mol)")


ax1.set_xticks([0.34,0.36,0.38,0.40,0.42])
ax1.set_yticks([0.0,-2,-4,-6])
# plt.xticks([0.0,1.0,2.0,3.0,4.0])
# plt.yticks([0,1,2,3,4,5,6])

# We change the fontsize of minor ticks label
# plt.tick_params(axis='both', which='major', labelsize=10)
# plt.tick_params(axis='both', which='minor', labelsize=8)
# plt.xticks(np.linspace(0.0,32.0,17),fontsize=10)
# ax1.set_xticks(np.linspace(0,32.0,17),fontsize=10)

# ax1.xaxis.set_major_locator(np.linspace(0.0,32.0,5.0))
# ax1.xaxis.set_minor_locator(np.linspace(0,32.0,17))

# majorFormatter = FormatStrFormatter('%d')
# minorLocator = matplotlib.ticker.MultipleLocator(0.3)


# majorLocator = matplotlib.ticker.MultipleLocator(0.1)
# majorLocatorx = matplotlib.ticker.MultipleLocator(0.02)
# ax1.xaxis.set_minor_locator(minorLocator)
# ax1.yaxis.set_minor_locator(minorLocator)
# ax1.yaxis.set_major_locator(majorLocator)
# ax1.xaxis.set_major_locator(majorLocatorx)

ax1.tick_params(which='both', width=3)
ax1.tick_params(which='major', length=9)
ax1.tick_params(which='minor', length=5, color='k')

# legend
# 1:
# handles, labels = ax1.get_legend_handles_labels()
# ax1.legend(handles, labels,prop={'size':10})
# 2:
# lst_labels = ['','',]
lst_labels = [r'$r_{o}$ = 0.380']
ax1.legend(lst_labels,loc=9,prop={'size':30})
# 3:
# lst_labels = [r'$\epsilon_{h}$ = 1.44']
leg = plt.gca().get_legend()
for label in leg.get_lines():
    label.set_linewidth(4.5)

# some lines in legend!
# print len(ax1.lines),ax1.lines
# lst_labels = ['0.3','0.4','0.5','0.6','0.7']
# for i,line in enumerate(ax1.lines[2:7]):
#     print lst_labels[i]
#     line.set_label(lst_labels[i])
ax1.legend()



def save_fig(i,subdir,fname):
    ''' Make subdir if necessary.
    '''
    if subdir == '':
        content_dir = my_dir
    else:
        content_dir = os.path.join('/'.join(my_dir.split('/')[0:i]),subdir)
    if not os.path.exists(content_dir): os.makedirs(content_dir)
    dir_filename = os.path.join(content_dir,fname)
    fp_filename = os.path.join(dir_filename,fname)
    if not os.path.exists(dir_filename): os.makedirs(dir_filename)
    # Save in PNG,EPS,SVG,PDF,TIFF,JPG formats
    # PIL, wxpython2.8, QT5Agg may be necessary
    # Image.open('%s.png' % fp_filename).save('%s.jpg' % fp_filename,'JPEG')
    # dpi = 300 # 300,900
    # matplotlib.rcParams['figure.dpi'] = 900
    dpi = matplotlib.rcParams['figure.dpi']
    plt.savefig('%s.png' % dir_filename,dpi=dpi)
    plt.savefig('%s.png' % fp_filename,dpi=dpi)
    plt.savefig('%s.eps' % fp_filename,dpi=dpi)
    plt.savefig('%s.svg' % fp_filename,dpi=dpi)
    plt.savefig('%s.pdf' % fp_filename,dpi=dpi)
    plt.savefig('%s.tiff' % fp_filename,dpi=dpi)
    plt.savefig('%s.jpg' % fp_filename,dpi=dpi)

if option == 'show':
    plt.show()
    sys.exit()
elif option == 'publish':
    matplotlib.rcParams['figure.dpi'] = 1200
    data_name = data_name + '_PUB'
    print "calling save_fig ..."
    # save_pic_data(levels_back,subdir,name)
    # example: save_fig(-4,'fig',name)
    # example: save_fig(-3,'',name)
    save_fig(0,'fig','%s_%s_%s' % (result_type,plot_type,data_name))
else:
    print 'saving dpi=300 (default) image ..'
    plt.savefig('fig/%s_%s_%s.png' % (result_type,plot_type,data_name))

# if sys.argv[1] == 'show':
#     plt.show()
#     sys.exit()
# elif sys.argv[1] == 'publish':
#     matplotlib.rcParams['figure.dpi'] = 1200
#     data_name = data_name + '_PUB'
#     print "calling save_fig ..."
#     # save_pic_data(levels_back,subdir,name)
#     # example: save_fig(-4,'fig',name)
#     # example: save_fig(-3,'',name)
#     save_fig(0,'fig','%s_%s_%s' % (result_type,plot_type,data_name))
# else:
#     print 'saving dpi=300 (default) image ..'
#     plt.savefig('fig/%s_%s_%s.png' % (result_type,plot_type,data_name))

#  ---------------------------------------------------------  #
#  mpl_myargs_end                                             #
#  ---------------------------------------------------------  #
if args['option'] == None:
    print 'saving (default) image .. dpi=%d' % matplotlib.rcParams['figure.dpi']
    plt.savefig('fig/%s_%s_%s.png' % (result_type,plot_type,data_name))
elif args['option'] == 'show':
    plt.show()
    sys.exit()
elif args['option'] == 'publish':
    matplotlib.rcParams['figure.dpi'] = 1200
    data_name = data_name + '_PUB'
    print "calling save_fig ..."
    # save_pic_data(levels_back,subdir,name)
    # example: save_fig(-4,'fig',name)
    # example: save_fig(-3,'',name)
    save_fig(0,'fig','%s_%s_%s' % (result_type,plot_type,data_name))
