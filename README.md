# CAD Blueprint Comparison Tool

## Overview

This project is a CAD drawing comparison tool designed to detect structural differences between two engineering drawings.

It was inspired by real-world exposure to building system layouts during my internship at L&T.

## Problem

Pixel-based comparison methods fail for CAD drawings due to:

* alignment issues
* repetitive patterns (grids, symbols)
* differences in drawing styles

## Approach

The project pivots from image comparison to **geometry-level analysis** using DXF files.

Key idea:

* Compare actual entities (lines, shapes) instead of pixels

## Current Progress

* Image-based comparison using OpenCV (initial approach)
* Identified limitations with alignment and accuracy
* Transitioning to DXF-based comparison using `ezdxf`

## Planned Features

* Layer-by-layer comparison
* Detection of added / removed / modified entities
* Visualization of differences

## Tech Stack

* Python
* OpenCV
* ezdxf

## Status

Work in progress — currently building DXF parsing and comparison pipeline.

## Author

~Sadhana K
