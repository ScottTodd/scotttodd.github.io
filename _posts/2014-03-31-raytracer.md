---
layout: post
title: Raytracer
tagline: Ray Tracing, Radiosity, and Photon Mapping in C++ and OpenGL.
description: Ray Tracing, Radiosity, and Photon Mapping in C++ and OpenGL.
category: projects
tags: [Graphics, C++, OpenGL]
title_images: [/assets/projects/raytracer/raytracing.png, /assets/projects/raytracer/radiosity.png]
tile_image: /assets/projects/raytracer/tile.png
---
{% include JB/setup %}

<div class="project-images">
    <figure>
        <img src="/assets/projects/raytracer/raytracing.png" title="Ray tracing with reflections and soft shadows" class="img-responsive img-responsive">
        <figcaption>Ray tracing with reflections and soft shadows</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/raytracer/raytracing-texture.png" title="Ray tracing using textures" class="img-responsive img-responsive">
        <figcaption>Ray tracing using textures</figcaption>
    </figure>
</div>

<h3>Overview</h3>

This was a <a href="http://www.cs.rpi.edu/~cutler/classes/advancedgraphics/S14/hw3_rendering.php">homework assignment</a> for <a href="http://www.cs.rpi.edu/~cutler/classes/advancedgraphics/S14/index.php">Advanced Computer Graphics</a>. This project focused on implementing rendering using ray tracing, radiosity, and photon mapping.

<h3>My Contributions</h3>

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

<div class="project-images">
    <figure>
        <img src="/assets/projects/raytracer/radiosity.png" title="Radiosity within the Cornell Box" class="img-responsive">
        <figcaption>Radiosity within the <a href="http://en.wikipedia.org/wiki/Cornell_box">Cornell box</a></figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/raytracer/radiosity-undistributed.png" title="Undistributed radiosity during iterative solving" class="img-responsive">
        <figcaption>Undistributed radiosity during iterative solving</figcaption>
    </figure>
</div>

<div class="project-images">
    <figure>
        <img src="/assets/projects/raytracer/photon-mapping.png" title="Photon mapping caustics using a reflective ring on a flat surface" class="img-responsive">
        <figcaption>Photon mapping caustics using a reflective ring</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/raytracer/photon-mapping-exaggerated.png" title="Photon mapping results exaggerated (upscaled)" class="img-responsive">
        <figcaption>Photon mapping results exaggerated (upscaled)</figcaption>
    </figure>
</div>
