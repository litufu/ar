# -*- coding: UTF-8 -*-

from project.data import context
from project.report import auditReport
from project.financialStatements import addFs
from project.notes import addNoteAccountingPolicy
from project.changeAndErrorCorrection import addChange
from project.tax import addTax
from project.combine import addCombine
from project.noteappended import addNoteAppended
from project.fsmodel import fillTable
from project.computeNo import computeNo

from project.constants import comparativeTable,tables,contrastSubjects,COMBINEPATH,SINGLEPATH,balanceTitlesState,balanceTitlesList,profitTitlesState,profitTitlesList


if __name__ == '__main__':

    # 公司类型：上市公司、国有企业
    companyType = context["report_params"]["companyType"]
    # 报告类型：合并、单体
    reportType = context["report_params"]["type"]
    # 报表类型：合并、单体、母公司
    fsType = context["fs_params"]["type"]
    # 添加报告
    document = auditReport()
    # 填充报表数据
    fillTable(context, comparativeTable, tables, contrastSubjects, COMBINEPATH, SINGLEPATH)
    # 计算附注编码
    computeNo(context, comparativeTable)
    # 添加报表
    addFs(document, context, comparativeTable, balanceTitlesState, balanceTitlesList, profitTitlesState,profitTitlesList)
    # 添加会计政策,返回政策编码
    num = addNoteAccountingPolicy(document,context,comparativeTable)
    # 添加会计政策变更
    addChange(document, num,context)
    # 添加税收政策
    addTax(document)
    # 国有企业添加企业合并及合并财务报表
    if companyType == "国有企业" and reportType == "合并":
        addCombine(document)
    # 添加财务报表注释
    if reportType=="合并":
        addNoteAppended(document, COMBINEPATH, context, comparativeTable, isAll=False)
    else:
        addNoteAppended(document, SINGLEPATH, context, comparativeTable, isAll=False)

    document.save("report.docx")
