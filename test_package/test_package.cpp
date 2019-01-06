#include <cstdlib>

#include <Magnum/Primitives/Icosphere.h>
#include <Magnum/Trade/MeshData3D.h>
#include <Magnum/GL/Renderer.h>

#include <Corrade/Utility/Debug.h>

int main() {
    Magnum::GL::Renderer::enable(Magnum::GL::Renderer::Feature::DepthTest);

    const Magnum::Trade::MeshData3D sphere = Magnum::Primitives::icosphereSolid(4);

    Corrade::Utility::Debug() << "Success";

    return EXIT_SUCCESS;
}
