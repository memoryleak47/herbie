cp "$1" egg-herbie/src/scheduler.rs

make install
racket -l herbie report bench out
