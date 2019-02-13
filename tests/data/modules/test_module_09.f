C File: test_module_09.f
C Purpose: This code is taken from the DSSAT file ModuleDefs.for.  It tests
C          the handling of multiple constant declarations.
C
C Compile and run this program as follows:
C
C    gfortran -c test_module_09.f     # << this will create a file "mymod9.mod"
C    gfortran test_module_09.f        # << this will create a file "a.out"
C
C The output generated by this program is (see test_module_09-OUT.txt):
C
C    20      24    9000     300       3
C  1000      42      40     500     500
C  3.1416   0.0175   1   2   2   3   3

!-------------------------------------------------------------------------------
      MODULE MYMOD9
      INTEGER, PARAMETER :: 
     &    NL       = 20,  !Maximum number of soil layers 
     &    TS       = 24,  !Number of hourly time steps per day
     &    NAPPL    = 9000,!Maximum number of applications or operations
     &    NCOHORTS = 300, !Maximum number of cohorts
     &    NELEM    = 3,   !Number of elements modeled (currently N & P)
!            Note: set NELEM to 3 for now so Century arrays will match
     &    NumOfDays = 1000, !Maximum days in sugarcane run (FSR)
     &    NStalks = 42,   !Maximum stalks per sugarcane stubble (FSR)
     &    EvalNum = 40,   !Number of evaluation variables
     &    MaxFiles = 500, !Maximum number of output files
     &    MaxPest = 500   !Maximum number of pest operations

      REAL, PARAMETER :: 
     &    PI = 3.14159265,
     &    RAD=0.0174532925

      INTEGER, PARAMETER :: 
         !Dynamic variable values
     &    RUNINIT  = 1, 
     &    INIT     = 2,  !Will take the place of RUNINIT & SEASINIT
                         !     (not fully implemented)
     &    SEASINIT = 2, 
     &    RATE     = 3,
     &    EMERG    = 3
      END MODULE MYMOD9

!-------------------------------------------------------------------------------
      PROGRAM PGM
      USE mymod9

 10   FORMAT (5(I6,2X))
 15   FORMAT (2(F8.4,X),5(I3,X))

      write (*,10) NL, TS, NAPPL, NCOHORTS, NELEM
      write (*,10) NumOfDays, NStalks, EvalNum, MaxFiles, MaxPest
      write (*,15) PI, RAD, RUNINIT, INIT, SEASINIT, RATE, EMERG

      stop
      end program PGM
!-------------------------------------------------------------------------------
