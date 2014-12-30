---
layout: post
title: Painterly Rendering
tagline: Real-time painterly rendering using WebGL.
description: Real-time painterly rendering using WebGL.
category: projects
tags: [Graphics, WebGL, CoffeeScript, three.js, Open Source]
title_images: [/assets/projects/painterly-rendering/magma-bunny.png, /assets/projects/painterly-rendering/the-scream.png]
tile_image: /assets/projects/painterly-rendering/tile.png
extra_js: [/assets/js/jquery.githubRepoWidget.min.js, /assets/projects/painterly-rendering/script/magma-bunny.js]
---
{% include JB/setup %}

<div class="project-images">
    <figure>
        <div id="glContainer" class="gl-container img-responsive" height="360px" width="360px"></div>
        <figcaption>Interactive <a href="http://en.wikipedia.org/wiki/Stanford_bunny">Stanford Bunny</a> (requires WebGL)</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/painterly-rendering/the-scream.png" class="img-responsive" height="360px" width="360px">
        <figcaption><a href="http://en.wikipedia.org/wiki/The_Scream"><i>The Scream</i></a> texture on a quad</figcaption>
    </figure>
</div>

<h3>Overview</h3>

This was my final project for <a href="http://www.cs.rpi.edu/~cutler/classes/advancedgraphics/S14/index.php">Advanced Computer Graphics</a> and <a href="http://www.cogsci.rpi.edu/~destem/gamearch/">Game Architecture</a>. I worked with @andy-hanson on this project over a one month period. We used <a href="http://threejs.org/">three.js</a>, <a href="http://coffeescript.org/">CoffeeScript</a>, and WebGL.

Click <a href="/assets/projects/painterly-rendering/painterly-rendering.pdf">here</a> to download our full report.

<div class="github-widget" data-repo="ScottTodd/PainterlyRendering"></div>

<h3>My Contributions</h3>

I implemented brush stroke layers, depth-filtering using a multi-pass rendering approach, texture sampling, and diffuse lighting on brush stroke particles. We both contributed to the write-up and I performed the LaTeX conversion. I also collected all of the models and brush stroke textures that we used.

<div class="project-images">
    <figure>
        <img src="/assets/projects/painterly-rendering/blue-teapot.png" class="img-responsive" height="390px" width="390px">
        <figcaption><a href="http://en.wikipedia.org/wiki/Utah_teapot">Utah Teapot</a> rendered using strokes of varying saturation</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/painterly-rendering/bronze-teapot.png" class="img-responsive" height="390px" width="390px">
        <figcaption>The Utah Teapot rendered to appear bronze</figcaption>
    </figure>
</div>

<div class="project-images">
    <figure>
        <img src="/assets/projects/painterly-rendering/grass-sphere.png" class="img-responsive">
        <figcaption>Sphere using a grass texture</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/painterly-rendering/torus-knot.png" class="img-responsive">
        <figcaption>Torus knot, showcasing rendering order</figcaption>
    </figure>
</div>

<div class="project-images">
    <figure>
        <img src="/assets/projects/painterly-rendering/bouncing-spheres.png" class="img-responsive">
        <figcaption><a href="http://cannonjs.org/">Cannon.js</a> integration</figcaption>
    </figure>
    <figure>
        <img src="/assets/projects/painterly-rendering/bunny-steps-anim-text.gif" class="img-responsive">
        <figcaption>Rendering process breakdown</figcaption>
    </figure>
</div>
