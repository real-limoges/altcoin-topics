#!/bin/sh

# This script builds the directory structure for sbt
# Also creates a barebones build.sbt file

mkdir -p src/{main,test}/{java,scala,resources}
mkdir lib project target

echo 'name := "Project"

version := "1.0"

scalaVersion := "2.10.0"' > build.sbt
