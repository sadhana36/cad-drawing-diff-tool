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

The project explores moving beyond image-based comparison toward **structure-aware analysis** of CAD data.

Key idea:

* Instead of comparing raw pixels, the focus is on understanding and comparing the underlying structure of drawings.

## Current Progress

* Image-based comparison using OpenCV (initial approach)
* Identified limitations with alignment and accuracy
* Exploring more robust approaches for structure-level comparison

## Planned Features

* Layer-aware comparison
* Detection of added / removed / modified elements
* Visualization of structural differences

## Tech Stack

* Python
* OpenCV

## Status

Actively developing — evolving from image-based comparison toward more robust structural analysis approaches

## Limitations

* Current implementation does not handle rotated or scaled drawings
* Matching logic is still basic and not tolerance-aware
* Complex structures are not fully supported yet

## Author

~Sadhana K
