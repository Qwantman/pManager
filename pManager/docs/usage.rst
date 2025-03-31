Usage
=====

This section provides examples and guidelines for using the pManager library.

Basic Usage
-----------

First, you need to initialize a new instance of the `fileParser` or `fileWriter` class depending on whether you're reading or writing to a `.qpmgr` file.

Reading from a `.qpmgr` file:

.. code-block:: python

    from pManager import fileParser
    parser = fileParser("file.qpmgr", ignoreExtension = False)

    # Get opened & closed ports
    openedPorts = parser.getOpenedPorts()
    closedPorts = parser.getClosedPorts()

    # Get list of services
    servicesList = parser.getServicesList()

    # Print beautifully-formated services list
    for _ in servicesList:
        print(f'{parser.getBeautifuledInfoByService(i)}\n')

Writing to a `.qpmgr` file:

.. code-block:: python

    from pManager import fileWriter

    # Setting up writer
    writer = fileWriter("file.qpmgr", autoFlush = True, ignoreExtension = False)

    # Add new service
    # "ServiceName" will be used as a key to bind ports
    writer.constructServiceObj("ServiceName", "ServiceDescription")

    # Add port to service.
    # On port adding, file'll be flushed with autoFlush = True
    writer.bindPortToService(
        serviceName = "ServiceName",
        portNum = 80,
        portProto = "TCP",
        openState = True,
        portDesc = "HTTP server"
    )

    # Or, with autoFlush = False
    writer.writeToFile()