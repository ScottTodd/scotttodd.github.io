---
layout: post
title: "Raytracer"
tagline: Ray Tracing, Radiosity, and Photon Mapping in C++ and OpenGL.
category: projects
tags: [Graphics, C++, OpenGL]
title_images: [/assets/projects/raytracer/raytracing.png, /assets/projects/raytracer/radiosity.png]
---
{% include JB/setup %}


<div class="project-figures">
    <figure>
        <img src="/assets/projects/raytracer/raytracing.png" title="Ray tracing with reflections and soft shadows" class="project-padded">
        <figcaption>Ray tracing with reflections and soft shadows</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/raytracer/raytracing-texture.png" title="Ray tracing using textures" class="project-padded">
        <figcaption>Ray tracing using textures</figcaption>
    </figure>
</div>

<hr>

This was a <a href="http://www.cs.rpi.edu/~cutler/classes/advancedgraphics/S14/hw3_rendering.php">homework assignment</a> for <a href="http://www.cs.rpi.edu/~cutler/classes/advancedgraphics/S14/index.php">Advanced Computer Graphics</a>. As part of this assignment, I implemented:

Ray Tracing

* Ray-sphere intersection testing
* Shadow and reflective rays
* Distribution ray tracing for soft shadows and antialiasing
* Stratified random sampling

Radiosity

* Form factor computation
* Iterative radiosity solving
* Occlusion ray casting

Photon Mapping

* Photon distribution throughout the scene
* Photon collection using a k-d tree

<hr>

<div class="project-figures">
    <figure>
        <img src="/assets/projects/raytracer/radiosity.png" title="Radiosity within the Cornell Box" class="project-padded" height="400px" width="400px">
        <figcaption>Radiosity within the <a href="http://en.wikipedia.org/wiki/Cornell_box">Cornell box</a></figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/raytracer/radiosity-undistributed.png" title="Undistributed radiosity during iterative solving" class="project-padded" height="400px" width="400px">
        <figcaption>Undistributed radiosity during iterative solving</figcaption>
    </figure>
</div>

<hr>

<div class="project-figures">
    <figure>
        <img src="/assets/projects/raytracer/photon-mapping.png" title="Photon mapping caustics using a reflective ring on a flat surface" class="project-padded" height="400px" width="400px">
        <figcaption>Photon mapping caustics using a reflective ring</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/raytracer/photon-mapping-exaggerated.png" title="Photon mapping results exaggerated (upscaled)" class="project-padded" height="400px" width="400px">
        <figcaption>Photon mapping results exaggerated (upscaled)</figcaption>
    </figure>
</div>
