# -*- coding: utf-8 -*-

{
    'name': 'Educational Exam Management',
    'version': '11.0.1.0.0',
    'summary': """Sneak the Examination management in Educational ERP""",
    'description': 'An easy way to handle the examinations in an educational '
                   'system with better reports and exam valuation and exam result '
                   'facilities',
    'category': 'Industries',
    'author': 'SM Ashraf',
    'company': 'Eagle It Solutions',
    'maintainer': 'Eagle ERP',
    'website': "https://www.eagle_erp.com",
    'depends': ['education_core'],
    'data': [
        'security/ir.model.access.csv',
        'data/education.result.grading.csv',
        'views/grade_configuration_view.xml',
        'views/examination.xml',
        'views/exam_valuation.xml',
        'views/exam_results.xml',
        'views/student_view.xml',
        'reports/exam_academic_transcript.xml',
        'reports/exam_academic_transcript1.xml',
        'reports/exam_evaluation.xml',
        'reports/merit_list.xml',
        'reports/exam_academic_transcript_s.xml',
        'reports/exam_academic_transcript_new.xml',
        'reports/report.xml',
        'wizards/academic_transcript_wizard.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
