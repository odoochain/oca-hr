import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-hr",
    description="Meta package for oca-hr Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-hr_branch>=15.0dev,<15.1dev',
        'odoo-addon-hr_contract_employee_calendar_planning>=15.0dev,<15.1dev',
        'odoo-addon-hr_contract_multi_job>=15.0dev,<15.1dev',
        'odoo-addon-hr_contract_reference>=15.0dev,<15.1dev',
        'odoo-addon-hr_course>=15.0dev,<15.1dev',
        'odoo-addon-hr_department_code>=15.0dev,<15.1dev',
        'odoo-addon-hr_emergency_contact>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_age>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_birth_name>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_calendar_planning>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_digitized_signature>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_document>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_firstname>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_id>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_lastnames>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_medical_examination>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_partner_external>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_phone_extension>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_relative>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_service>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_service_contract>=15.0dev,<15.1dev',
        'odoo-addon-hr_employee_ssn>=15.0dev,<15.1dev',
        'odoo-addon-hr_holidays_settings>=15.0dev,<15.1dev',
        'odoo-addon-hr_job_category>=15.0dev,<15.1dev',
        'odoo-addon-hr_org_chart_overview>=15.0dev,<15.1dev',
        'odoo-addon-hr_personal_equipment_request>=15.0dev,<15.1dev',
        'odoo-addon-hr_study>=15.0dev,<15.1dev',
        'odoo-addon-hr_worked_days_from_timesheet>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
