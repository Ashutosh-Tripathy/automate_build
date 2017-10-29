import os
import sys
import subprocess
import logging



# --------------------------------------------------------------------------------------------------
# One time change.
# Dirctory structure of projects (change if you want different structure).
base_path = 'c:/csi/'
# for linux
#base_path = '/home/astr/csi/'
project_path = {'ee' : 'ee/', 'cui' : 'cui/'}
sub_project_path = {'core' : 'c/', 'policy' : 'p/', 'websecurity' : 'w/', '' : ''}
# --------------------------------------------------------------------------------------------------





# --------------------------------------------------------------------------------------------------
# Frequently changed.
story_path = 'stories/'
# for trunk
# story_path = ''
story_name = 'B-300325.Spartans_Improve_FVT_automation/'
# for trunk
# story_name = 'trunk/'


operations = [
    # Comment operation you do not want to perform. Ex below:
    # 'checkout',
    # 'checkout',
    # 'update',
    'build'
]

projects = [
    # Comment project if you want t skip(no need to comment sub projects) Ex below:
    # 'ee'
    'ee',
    'cui'
]

sub_projects = {
    'ee' : [''],
    'cui' : [
                # Comment sub_project if you want to skip. Ex below:
                # 'core',
                'core',
                'policy',
                'websecurity'
            ]
}

sub_projects2 = {
    '' : [
        'com.mcafee.csi.parent-resources',
        'com.mcafee.csi.parent'],

    'core': [
        # Comment the sub project name if you do not want to skip. Ex below:
        # 'commonui-core_parent'
        'commonui-core_parent',
        'commonui-core-ui',
        'commonui-core',
        'commonui-core_testlib',
        ],
    'policy': [
        'commonui-policy_parent',
        'commonui-policy-ui',
        'commonui-policy',
    ],

    'websecurity' : [
        'commonui-websecurity_parent',
        'rest',
        'commonui-websecurity-ui',
        'commonui-websecurity',
        'commonui-websecuritytest'
    ]
}

operation_commands = {
    # replace command if you want to customize
    # 'build': 'mvn clean install -P !jsduck'
    'checkout' : 'svn checkout ',
    'update': 'svn update ',
    'build': 'mvn clean install -DskipTests'
}
# ---------------------------------------------------------------------------------------------





# ---------------------------------------------------------------------------------------------
# Rarely changed
sub_project2_path = {
    'com.mcafee.csi.parent-resources' : 'csidev/source/com.mcafee.csi.parent-resources',
    'com.mcafee.csi.parent' : 'csidev/source/com.mcafee.csi.parent',
    'commonui-core_parent' : 'source/commonui-core_parent/',
    'commonui-core-ui' : 'source/extensions/commonui-core/ui/',
    'commonui-core' : 'source/extensions/commonui-core',
    'commonui-core_testlib' : 'source/commonui-core_testlib/',
    'commonui-policy_parent' : 'source/commonui-policy_parent/',
    'commonui-policy-ui' : 'source/extensions/commonui-policy/ui/',
    'commonui-policy' : 'source/extensions/commonui-policy/',
    'commonui-websecurity_parent' : 'source/commonui-websecurity_parent/',
    'rest' : 'source/extensions/commonui-websecurity/rest/',
    'commonui-websecurity-ui' : '/source/extensions/commonui-websecurity/ui/',
    'commonui-websecurity' : '/source/extensions/commonui-websecurity/',
    'commonui-websecuritytest' : 'source/extensions/commonui-websecuritytest/'

}

base_repo = 'https://bansource3.corp.nai.org/svn/projects/csi/'
project_repo = {'ee' : 'EmailEncryption/', 'cui' : 'CommonUI/'}
sub_project_repo = {'' : '', 'core' : 'Core/', 'policy' : 'Policy/', 'websecurity' : 'WebSecurity/'}
# --------------------------------------------------------------------------------------------






logging.basicConfig(format='%(levelname)s - %(message)s', filename='build_script.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger('log.log')
stderr_log_handler = logging.StreamHandler()
logger.addHandler(stderr_log_handler)

create_path_automatically = False

# Create and return svn repo url.
def get_repo_url(project, sub_project):
    return base_repo + project_repo[project] + sub_project_repo[sub_project] + story_path + story_name

# Create and return directory path for project
def get_path(operation, project, subproject, sub_project2):
    path = base_path + project_path[project] + sub_project_path[subproject] + story_path
    if (operation == 'build'):
        path += story_name + sub_project2_path[sub_project2]
    elif (operation == 'update'):
        path += story_name
    return path

# Confirm whether to create path automatically or not.
def confirm_path_creation(path):
    global create_path_automatically
    logger.info('Path not found: ' + path)
    while True:
        char = input("Press y to create path or n to exit.......")
        if (char == 'y'):
            create_path_automatically = True
            return
        elif (char == 'n'):
            sys.exit()

# Check command execution status and act accordingly.
def handle_command_status(status):
    if (status == 0):
        logger.info("Operation completed successfully.")
    else:
        logger.error("Error while executing command. Check console for more details.")
        sys.exit()

# Validate path and create if not present for checkout operaion.
def handle_path_validation_and_creation(operation, path):
    if (not os.path.isdir(path)):
        if (operation == 'checkout'):
            if (not create_path_automatically):
                confirm_path_creation(path)
            logger.debug('Path not exist. Createing path: ' + path)
            os.makedirs(path)
        else:
            logger.error('Path not exist: ' + path)
            sys.exit()

def performOperation(operation, project, sub_project, sub_project2 = ''):
    logger.debug("=" * 80)
    logger.info('Operation: ' + operation + ' ' + project +  ' ' + sub_project + ' ' + sub_project2)
    path = get_path(operation, project, sub_project, sub_project2)
    handle_path_validation_and_creation(operation, path)

    command = operation_commands[operation] + get_repo_url(project, sub_project) if operation == 'checkout' else operation_commands[operation]
    logger.info("Path: " + path)
    logger.info("Command: " + command)
    os.chdir(path)
    status = subprocess.call(command.split(), shell = True)
    # On linux
    # status = subprocess.call(command.split())
    handle_command_status(status)
    logger.debug("=" * 80 + "\n\n\n\n\n")
    # input("press a key......")


# Execute command  on each project for each opeartion
for operation in operations:
    for project in projects:
        for sub_project in sub_projects[project]:
            if operation == 'build':
                for sub_project2 in sub_projects2[sub_project]:
                    performOperation(operation, project, sub_project, sub_project2)
            else:
                performOperation(operation, project, sub_project)