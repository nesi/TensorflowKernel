#!/bin/bash
module purge
module load $1
shift
exec $@