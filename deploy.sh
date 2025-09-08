#!/bin/bash
./package.sh
RESOURCEGROUPNAME=functionapp-rg
FUNCTIONAPPNAME=python-function-app-qhm08h
ZIPPATH=package.zip
az functionapp deployment source config-zip -g "$RESOURCEGROUPNAME" -n "$FUNCTIONAPPNAME" --src "$ZIPPATH" --build-remote true
