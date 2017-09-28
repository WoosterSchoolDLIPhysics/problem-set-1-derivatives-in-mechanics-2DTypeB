# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:17:24 2017

@author: acgnm
"""

from pylab import *

def Q1():
    
    t = linspace(0, 4, 1000)
    
    dt = 0.01
    
    def x(t):
        return t**4 - 4*t**3 + 2*t**2 + 3*t + 6
    
    def v(t):
        return 4*t**3 - 12*t**2 + 4*t + 3
    
    def a(t):
        return 12*t**2 - 24*t + 4
        
    def jerk(t):
        return 24*t - 24
        
    fx = x(t)
    fv = v(t)
    fa = a(t)
    fj = jerk(t)
    
    def Q1Figure():
        
        figure('Question 1')
        clf()
        subplot(411)
        plot(t, fx)
        grid()
        ylabel('x(t)')
        xlabel('t')
        
        subplot(412)
        plot(t, fv)
        grid()
        ylabel('v(t)')
        xlabel('t')
        
        subplot(413)
        plot(t, fa)
        grid()
        ylabel('a(t)')
        xlabel('t')
        
        subplot(414)
        plot(t, fj)
        grid()
        ylabel('jerk(t)')
        xlabel('t')
        
        return True
    
    Q1Figure()

    return True

Q1()

def Q2():
    
    t0 = 0.0 #initial time
    tf = 50.0 # Final Time
    dt = 1. # step
    t = arange(t0, tf, dt) # make an array
    v = zeros(len(t)) # make a bunch of 0
    
    #define some constant
    b = 0.10 # random constant
    g = 10 #m/s^2
    m = 1.0 #kg
    
    for i in arange(1,len(t)):
        
        dv = (-b/m*v[i-1]-g)*dt
        v[i] = v[i-1] + dv
    
    figure('Question 2')
    clf()
    subplot(111)
    plot(t, v, 'ko')
    vt = -m*g/b
    plot(t, vt*(1-exp(-b*t/m)),'b', lw =3)
    text(20, -40, r'$v(t) = v_T(e^{-\frac{bt}{m}}-1)$', size = 20, color='Maroon')
    plot(t, 0*t + vt, 'k--')
    plot(t, -g*t, 'c--')
    grid()
    xlabel('t')
    ylabel('v(t)')
    ylim(-120.0)
    
    return True
    
Q2()

def Q4():
    
    t = linspace(0,1,1000)
    
    x = 3*sin(2*pi*t)
    vx = 6*pi*cos(2*pi*t)
    ax = -12*pi*pi*sin(2*pi*t)
    y = 2*cos(2*pi*t)
    vy = -4*pi*sin(2*pi*t)
    ay = -8*pi*pi*cos(2*pi*t)
    
      
    for i in range(len(t)):
        figure('Question 4')
        clf()
        plot(x,y,'r-')
        plot(vx,vy)
        plot(ax,ay)
        plot([0,x[i]],[0,y[i]],'b-o')
        plot([0,vx[i]],[0,vy[i]],'r-o')
        plot([0,ax[i]],[0,ay[i]],'g-o')
        grid()
        savefig('frame_%03d.png' % it)
        
        pause(0.01)
    
    return True

Q4()