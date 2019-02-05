#include <cstdlib>

#include <Magnum/Primitives/Icosphere.h>
#include <Magnum/Trade/MeshData3D.h>

#include <Corrade/Utility/Debug.h>

int main() {
    const Magnum::Trade::MeshData3D sphere = Magnum::Primitives::icosphereSolid(4);

    Corrade::Utility::Debug() << "Success";

    return EXIT_SUCCESS;
}
